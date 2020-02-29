# ParseOutput.py
#
# Removes the quotes from the lat/lon

import csv

strInFile = "../output.csv"
strOutFile = "parsedOutput.csv"


with open(strOutFile, 'w+') as outFile:
	for line in open(strInFile, 'r'):
		line = line.replace('"', '').strip()
		outFile.write(line + '\n')