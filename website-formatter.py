import csv, sys, socket
from ip2geotools.databases.noncommercial import DbIpCity

with open(sys.argv[1]) as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        try:
            ip = socket.gethostbyname(row['domain'])
        except:
            ip = "domain did not resolve"

        coordinates = None
        if not row['lat'] and not row['lng']:
            try:
                coordinates = DbIpCity.get(ip, api_key='free')
            except:
                pass
        
        if coordinates:
            print(row['domain'] + ", " + str(coordinates.latitude) + ", " + str(coordinates.longitude) + ", " + row['locationVerified'] + ", " + ip)
        else:
            print(row['domain'] + ", " + row['lat'] + ", " + row['lng'] + ", " + row['locationVerified'] + ", " + ip)