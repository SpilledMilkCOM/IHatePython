import sys

from models.Resource import Resource
from utils.craftUtil import craft_calc
from utils.mockUtil import create_items_from_json, create_levels_from_json, create_warrior_from_json

warrior = None
levels = None
itemResources = None
usedResources = None

def load_files(itemFileName: str, levelFileName: str, itemResourcesFileName: str, usedResourcesFileName: str):

    global warrior, levels, itemResources, usedResources

    file = open(itemFileName, "r")
    warrior = create_warrior_from_json(file.read())

    file =  open(levelFileName, "r")
    levels = create_levels_from_json(file.read())

    if (itemResourcesFileName != None):
        file =  open(itemResourcesFileName, "r")
        itemResources = create_items_from_json(file.read())
    
    if (usedResourcesFileName != None):
        file =  open(usedResourcesFileName, "r")
        usedResources = create_warrior_from_json(file.read())

def main(itemFileName: str, levelFileName: str, itemResourcesFileName: str, usedResourcesFileName: str):
    """Given the item filename, determine the levels to run in order to gain the resources to create the item.
    
    Args:
        itemFileName (str): The file name of the item (JSON format)
        levelFileName (str): The file name of the levels (JSON format)
        itemResourcesFileName (str): The file name of the items that can be created from other items (JSON format)
        usedResourcesFileName (str): The file name of the items that have already been retrieved (JSON format)
    """
    global warrior

    print(f"\n\nInputs: '{itemFileName}', '{levelFileName}', '{usedResourcesFileName}'\n")

    load_files(itemFileName, levelFileName, itemResourcesFileName, usedResourcesFileName)

    print(warrior)
    print(usedResources)

    warrior += usedResources

    print(warrior)
    
    for item in itemResources:
        print(item)

    craft_calc(warrior, levels)

    # print(repr(warrior))
    # for level in levels:
    #     print(repr(level))

if (__name__ == '__main__'):
    if (len(sys.argv) < 2):
        main("warrior.json", "levels.json", None, None)
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
