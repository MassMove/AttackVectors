import json, csv


sites = {}
sites = []
with open("sites.csv", "r") as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        try:
            sites.append([row['domain'], float(row['lat']), float(row['lng'])])
        except ValueError: # for sites that dont have location
            pass

with open("sites-geocoded.json", "w") as jsonfile:
    json.dump(sites, jsonfile, indent=4)