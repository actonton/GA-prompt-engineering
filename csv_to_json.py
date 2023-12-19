import csv
import json

file = 'imdb_movies.csv'
json_file = 'imdb_movies.json'


#Prep to Ingest the csv into the vector database as json objects
#Run only if no json exists

#Read CSV File
def read_CSV(file, json_file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        convert_write_json(csv_rows, json_file)

#Convert csv data into json
def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))) #for pretty
        f.write(json.dumps(data))


read_CSV(file,json_file)