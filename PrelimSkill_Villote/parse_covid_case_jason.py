import json
import csv

JSON_FILE_PATH = './covid_cases.json'
with open(JSON_FILE_PATH) as infile:
    covid_cases = json.loads(infile.read())

CSV_FILE_PATH = './covid_cases_(fromJSON).csv'
with open(CSV_FILE_PATH, 'w') as outputfile:
    file = csv.writer(outputfile)

    file.writerow(["date", "countries/Terrorie", "cases", "deaths"])

    for record in covid_cases["records"]:
        file.writerow([record["dateRep"], record["countriesAndTerritories"], record["cases"], record["deaths"]])