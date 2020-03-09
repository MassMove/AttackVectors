import csv, sys, socket, json
from ip2geotools.databases.noncommercial import DbIpCity
from passivetotal.libs.attributes import AttributeRequest

with open(sys.argv[1]) as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        # Get the IP address of the domain name
        try:
            ip = socket.gethostbyname(row['domain'])
        except:
            ip = "domain did not resolve"

        # Get geo-coordinates of the IP address
        coordinates = None
        if not row['lat'] and not row['lng']:
            try:
                coordinates = DbIpCity.get(ip, api_key='free')
            except:
                pass
        
        # Gather web trackers (Google Analytics Tracking ID, FacebookId, etc.)
        trackers = ""
        print(trackers)
        csv_row = ""
        if coordinates:
            csv_row = row['domain'] + ", " + str(coordinates.latitude) + ", " + str(coordinates.longitude) + ", " + row['locationVerified'] + ", " + ip
        else:
            csv_row = row['domain'] + ", " + row['lat'] + ", " + row['lng'] + ", " + row['locationVerified'] + ", " + ip
        if "GoogleAnalyticsAccountnNumber" in trackers.values():
            csv_row = csv_row + ", " + trackers['GoogleAnalyticsAccountNumber']
        else:
            csv_row = csv_row + ", , "
        if "GoogleAnalyticsTrackingId" in trackers.values():
            csv_row = csv_row + ", " + trackers['GoogleAnalyticsTrackingId']
        else:
            csv_row = csv_row + ", , "
        if "AddThisPubID" in trackers.values():
            csv_row = csv_row + ", " + trackers['AddThisPubId']
        else:
            csv_row = csv_row + ", , "
        if "FacebookId" in trackers.values():
            csv_row = csv_row + ", " + trackers['FacebookId']
        else:
            csv_row = csv_row + ", , "
        if "TwitterId" in trackers.values():
            csv_row = csv_row + ", " + trackers['TwitterId']
        else:
            csv_row = csv_row + ", , "
        
        print(csv_row)
