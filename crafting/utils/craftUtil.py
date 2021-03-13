import math

from models.BestLevel import BestLevel
from models.Item import Item

def craft_calc(item: Item, levels, items):
    print("\nCalculating...\n\n")

    # Which levels have the resources needed?
    # Add BestLevel to a dictionary (resource name, level name, amount per unit cost)

    best = {}

    for neededResource in item.resources:
        for level in levels:
            for levelResource in level.resources:
                if (neededResource.name == levelResource.name):
                    if (neededResource.name not in best):
                        best[neededResource.name] = BestLevel(level.name, neededResource.name, ((levelResource.min + levelResource.max) / 2) / level.cost, (levelResource.min + levelResource.max) / 2)
                    elif (best[neededResource.name].unit < ((levelResource.min + levelResource.max) / 2) / level.cost):
                        best[neededResource.name] = BestLevel(level.name, neededResource.name, ((levelResource.min + levelResource.max) / 2) / level.cost, (levelResource.min + levelResource.max) / 2)

    for level in best.values():
        print(f"{level}")

    print("")

    # Will need to build a game tree of all of the possible runs to find out the best set of level runs

    # Will also need to figure out the resources that build other resources
    # Note the formatting below (< left justified -- > right justified)

    for neededResource in item.resources:
        level = best[neededResource.name]
        print(f"{neededResource.min:>4} {neededResource.name:<6} run level {level.level:<6} {math.ceil(neededResource.min / level.average):>3} times")

    print("")

    # Run levels that have resources that cannot be constructed

    itemsDict = {}

    for resource in items:
        itemsDict[resource.name] = resource

    for neededResource in item.resources:
        resource = itemsDict.get(neededResource.name)

        if (resource is None):
            level = best[neededResource.name]
            run_level(find_level(level.level, levels), item, math.ceil(neededResource.min / level.average))

    print(item)

    # Anything that's a surplus (a negative amount),  convert it to a resource that needs it.

    print("\n\n")

    return None

def find_level(name: str, levels):
    for level in levels:
        if (level.name == name):
            return level
    return None

def run_level(level, item, count: int):

    print(f"Running Level '{level.name}' {count} times...")

    for resource in level.resources:
        item.add_to_resource(resource.name, count * -resource.average())