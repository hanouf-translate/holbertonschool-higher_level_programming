import json 
""" basic serialization module"""

def serialize_and_save_to_file(data, filename):
    """ this method converts dict formated data to JSON """

    with open(filename, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile)


def load_and_deserialize(filename):
    """ load and deserialize data from the specified file from JSON file to py dict"""
    with open(filename, mode='r', encoding="utf-8") as json_file:
        dict_data = json.load(json_file)
    return dict_data    
        
    
    
if __name__=="__main__":
    data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
    }
    deserialized_data = load_and_deserialize('data.json')
    print("Deserialized Data:")
    print(deserialized_data)

