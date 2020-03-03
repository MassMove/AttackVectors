import json, csv


sites = {}
sites = []
with open("sites-geocoded.csv", "r") as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        try:
            # sites[row[0]] = {"lat" : float(row[1]), "lon" : float(row[2])}
            sites.append([row[0], float(row[1]), float(row[2])])
        except ValueError: # for sites that dont have location
            pass

with open("sites-geocoded.json", "w") as jsonfile:
    json.dump(sites, jsonfile)



