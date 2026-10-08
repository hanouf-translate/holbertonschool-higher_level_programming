import csv 
import json 

def convert_csv_to_json(csv_filename, json_filename="data.json"):
    """Converting CSV Data to JSON Format"""
    try:
            with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                data = list(reader)  # Reads CSV rows into a list of dictionaries

            with open(json_filename, mode='w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4)

            return True

        except Exception:
            return False
