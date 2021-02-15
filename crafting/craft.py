import sys

from models.Resource import Resource
from utils.craftUtil import craft_calc
from utils.mockUtil import create_warrior, create_levels_from_json, create_warrior_from_json, create_warrior_from_json2

warrior = None
levels = None
usedResources = None

def load_files(itemFileName: str, levelFileName: str, usedResourcesFileName: str):

    global warrior, levels, usedResources

    file = open(itemFileName, "r")
    warrior = create_warrior_from_json(file.read())

    file =  open(levelFileName, "r")
    levels = create_levels_from_json(file.read())
    
    if (usedResourcesFileName != None):
        file =  open(usedResourcesFileName, "r")
        usedResources = create_warrior_from_json(file.read())

def main(itemFileName: str, levelFileName: str, usedResourcesFileName: str):
    """Given the item filename, determine the levels to run in order to gain the resources to create the item.
    
    Args:
        itemFileName (str): The file name of the item (JSON format)
        levelFileName (str): The file name of the levels (JSON format)
    """
    global warrior

    print(f"\n\nInputs: '{itemFileName}', '{levelFileName}', '{usedResourcesFileName}'\n")

    load_files(itemFileName, levelFileName, usedResourcesFileName)

    print(warrior)
    print(usedResources)

    warrior += usedResources

    print(warrior)
    
    # for level in levels:
    #     print(level)

    craft_calc(warrior, levels)

    # print(repr(warrior))
    # for level in levels:
    #     print(repr(level))

if (__name__ == '__main__'):
    if (len(sys.argv) < 2):
        main("warrior.json", "levels.json", None)
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
