import json

from models.Item import Item
from models.Level import Level
from models.Resource import Resource

def craft_calc(item, levels):
    print("\nCalculating...\n")

    # Which levels have the resources needed?

    # Loop through the item's resources and just spit out the level of resource and how many times it's needed.
    
    for needed in item.resources:
        for level in levels:
            for resource in level.resources:
                if (needed.name == resource.name):
                    print(f"Level={level.name} x {needed.min / ((resource.min + resource.max) / 2):.1f} -- {needed.name}")

    print("\nEfficiences:\n")

    # Find the level that produces the most efficient result of a resource.

    for level in levels:
            for resource in level.resources:
                print(f"Level={level.name} -- {resource.name} {((resource.min + resource.max) / 2) / level.cost}")

    print("\nBEST:\n")

    # Add tuples of 3 into a "best" dictionary (resource name, level name, amount per unit cost)
    # Create a tuple, versus creating a specialized object to contain those three pieces of info.

    best = {}

    for neededResource in item.resources:
        for level in levels:
            for levelResource in level.resources:
                if (neededResource.name == levelResource.name):
                    if (neededResource.name not in best):
                        best[neededResource.name] = (neededResource.name, level.name, ((levelResource.min + levelResource.max) / 2) / level.cost)
                    elif (best[neededResource.name][2] < ((levelResource.min + levelResource.max) / 2) / level.cost):
                        best[neededResource.name] = (neededResource.name, level.name, ((levelResource.min + levelResource.max) / 2) / level.cost)

    for level in best.values():
        print(f"{level[0]} in level {level[1]} @ {level[2]:.2f} / unit (cost)")

    # Will need to build a game tree of all of the possible runs to find out the best set of level runs

    # Will also need to figure out the resources that build other resources

    print("\n\n")

    return None