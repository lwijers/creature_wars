import base
import csv

# class Level_mngr:
#     def __init__(self, stage):
#
#         self.stage = stage

def create_lvl(stage, lvl):
    constructed_level = []
    with open('resources/csv/levels.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        next(csvReader, None)  # skip the headers
        for row in csvReader:
            print(lvl, type(lvl), row[0], type(row[0]))
            if row[0] == lvl:
                constructed_level.append(
                    base.Base(
                        stage,
                        int(row[2]),
                        int(row[3]),
                        str(row[1]),
                        int(row[4])
                    )
                )
    return constructed_level
