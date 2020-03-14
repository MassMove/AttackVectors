import csv
import sys
import pycristoforo as pyc

location = sys.argv[1]
quantity = int(sys.argv[2])

response_data = []
country_shape = pyc.get_shape(location)
coordinates = pyc.geoloc_generation(country_shape, quantity, location)

print("")
print("Generating", quantity, "points", "for", location, ":")

for coordinate in coordinates:
    csv_row = {}
    csv_row["location"] = location
    csv_row["lat"] = coordinate["geometry"]["coordinates"][1]
    csv_row["lng"] = coordinate["geometry"]["coordinates"][0]
    response_data.append(csv_row)
    print(csv_row)

print("")
print("Writing points to " + location + "-random-coordinates.csv:")

with open(location + "-random-coordinates.csv", mode="w") as new_csv_file:
    fieldnames = ["location", "lat", "lng"]
    writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, restval=None, extrasaction='ignore', lineterminator='\n')
    writer.writeheader()
    for element in response_data:
        writer.writerow(element)
        print(element["location"], element["lat"], element["lng"])
		
print("\r\nThis is our world now!\r\n")