import json


def load_json_file(filename):
    with open(filename) as file:
        return json.load(file)
