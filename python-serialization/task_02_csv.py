#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(filename):
    try:
        data = []
        with open(filename, 'r') as fcsv:
            reader = csv.DictReader(fcsv)
            for row in reader:
                data.append(row)
        with open("data.json", 'w') as f:
            f.write(json.dups(data, indent=4))
    except Exception:
        return False
    return True
