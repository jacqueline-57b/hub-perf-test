import json


def get_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config
