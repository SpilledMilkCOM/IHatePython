import sys

from models.Resource import Resource
from utils.craftUtil import craft_calc
from utils.mockUtil import create_warrior, create_levels_from_json, create_warrior_from_json, create_warrior_from_json2

warrior = None
levels = None

def load_files(itemFileName: str, levelFileName: str):

    global warrior, levels

    file = open(itemFileName, "r")

    warrior = create_warrior_from_json(file.read())

    file =  open(levelFileName, "r")

    levels = create_levels_from_json(file.read())

def main(itemFileName: str, levelFileName: str):
    """Given the item filename, determine the levels to run in order to gain the resources to create the item.
    
    Args:
        itemFileName (str): The file name of the item (JSON format)
        levelFileName (str): The file name of the levels (JSON format)
    """
    print(f"\n\nInputs: {itemFileName}\n")

    load_files(itemFileName, levelFileName)

    print(warrior)
    
    for level in levels:
        print(level)

    craft_calc(warrior, levels)

    print(repr(warrior))
    for level in levels:
        print(repr(level))

if (__name__ == '__main__'):
    if (len(sys.argv) < 2):
        main("warrior.json", "levels.json")
    else:
        main(sys.argv[1], sys.argv[2])
