import csv, sys, socket, json
from ip2geotools.databases.noncommercial import DbIpCity
from passivetotal.libs.attributes import AttributeRequest

response_data = []

with open(sys.argv[1]) as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        if "processed" not in row.keys():
            row["processed"] = False
        if row["processed"] == "False":
            # Get the IP address of the domain name
            try:
                ip = socket.gethostbyname(row['domain'])
            except:
                ip = "domain did not resolve"

            # Get geo-coordinates of the IP address
            coordinates = None
            if not row['latitude'] and not row['longitude']:
                try:
                    coordinates = DbIpCity.get(ip, api_key='free')
                except:
                    pass
            
            # Gather web trackers (Google Analytics Tracking ID, FacebookId, etc.)
            username = ""
            api_key = ""
            trackers = AttributeRequest(username=username, api_key=api_key).get_host_attribute_trackers(query=row['domain'])

            # Create dictionary that will be written at the end of processing the entire file.
            # We do this because the RiskIQ Tracker API call can return a varying amount of fields
            # so we don't know what headers to write in the CSV file until the processing is complete.
            csv_row = {}
            csv_row["domain"] = row['domain']
            csv_row["ip"] = ip
            csv_row["locationVerified"] = row['locationVerified']

            if coordinates:
                csv_row["latitude"] = str(coordinates.latitude) 
                csv_row["longitude"] = str(coordinates.longitude)
            else:
                csv_row["latitude"] = row['latitude']
                csv_row["longitude"] = row['longitude']

            if "status" in trackers:
                csv_row["processed"] = False
            elif "success" in trackers:
                for tracker in trackers["results"]:
                    if tracker["attributeType"] == "GoogleAnalyticsTrackingId":
                        csv_row["GoogleAnalyticsTrackingId"] = tracker['attributeValue']
                    if tracker["attributeType"] == "AddThisPubID":
                        csv_row["AddThisPubID"] = tracker['attributeValue']
                    if tracker["attributeType"] == "FacebookId":
                        csv_row["FacebookId"] = tracker['attributeValue']
                    if tracker["attributeType"] == "TwitterId":
                        csv_row["TwitterId"] = tracker['attributeValue']
            
            row["processed"] == "True"
            response_data.append(csv_row)
    
    #sys.argv[2]
    with open("processed.csv", mode='w') as new_csv_file:
        fieldnames = ['domain', 'ip', 'latitude', 'longitude', 'locationVerified', 'processed', 'GoogleAnalyticsTrackingId', 'AddThisPubID', 'FacebookId', 'TwitterId' ]
        writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, restval=None, extrasaction='ignore')
        writer.writeheader()
        for element in response_data:
            writer.writerow(element)