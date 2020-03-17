import json


def read_json_file(path):
    with open(path, 'r') as input_file:
        data = json.load(input_file)
    return data
