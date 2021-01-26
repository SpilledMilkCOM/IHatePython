import json
import sys

from utils.mockUtil import create_warrior, create_levels_from_json, create_warrior_from_json, create_warrior_from_json2

def load_files(itemFileName: str, levelFileName: str):
    file = open(itemFileName, "r")

    warrior = create_warrior_from_json(file.read())

    file =  open(levelFileName, "r")

    levels = create_levels_from_json(file.read())

    for level in levels:
        print(level.to_string())

    return warrior

def main(itemFileName: str, levelFileName: str):
    """Given the item filename, determine the levels to run in order to gain the resources to create the item.
    
    Args:
        itemFileName (str): The file name of the item (JSON format)
        levelFileName (str): The file name of the levels (JSON format)
    """
    print(f"\n\nInputs: {itemFileName}\n")

    warrior = load_files(itemFileName, levelFileName)

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
        main("warrior.json", "levels.json")
    else:
        main(sys.argv[1], sys.argv[2])
