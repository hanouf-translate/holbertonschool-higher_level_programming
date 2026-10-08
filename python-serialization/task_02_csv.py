import csv
import json


def convert_csv_to_json(csv_filename, json_filename="data.json"):
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            data = list(csv.DictReader(csv_file))

        with open(json_filename, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False