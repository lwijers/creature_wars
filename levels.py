import base
import csv

def create_lvl(lvl):
    constructed_level = []
    with open('resources/csv/levels.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        next(csvReader, None)  # skip the headers
        for row in csvReader:
            if row[0] == lvl:
                constructed_level.append(
                    base.Base(
                        lvl,
                        int(row[2]),
                        int(row[3]),
                        str(row[1]),
                        int(row[4])
                    )
                )
    return constructed_level
