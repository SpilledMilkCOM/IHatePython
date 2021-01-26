import json
import sys

from utils.mockUtil import create_warrior, create_warrior_from_json, create_warrior_from_json2

def load_file(fileName: str):
    file = open(fileName, "r")

    return create_warrior_from_json(file.read())

def main(fileName: str):
    """Given the item filename, determine the levels to run in order to gain the resources to create the item.
    
    Args:
        fileName (str): The file name of the item (JSON format)
    """
    print(f"\n\nInputs: {fileName}\n")

    warrior = load_file(fileName)

    print(warrior.to_string())

def print_mock_warrior():
    warrior = create_warrior()

    print(warrior.to_string())

    print(json.dumps(warrior, default=lambda childObj: childObj.__dict__, indent=4))

    # Alphabetical fields
    # print(json.dumps(warrior, default=lambda childObj: childObj.__dict__, indent=4, sort_keys=True))

    data = json.dumps(warrior, default=lambda childObj: childObj.__dict__)

    warrior = create_warrior_from_json2(data)

    print(warrior.to_string())

if (__name__ == '__main__'):
    if (len(sys.argv) < 2):
        main("warrior.json")
    else:
        main(sys.argv[1])
