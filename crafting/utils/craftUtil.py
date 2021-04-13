import math

from models.BestLevel import BestLevel
from models.Item import Item
from models.Level import Level

def convert_resource(itemWithNeededResource: Item, surplusResource, item: Item):
    """ Convert a surplus resource into a needed resource.

        Args:
            itemWithNeededResource (Item): 
            surplusResource ():
            item ():
    """
    value = surplusResource.average() / itemWithNeededResource.resource(surplusResource.name).average()

    item.add_to_resource(itemWithNeededResource.name, value)
    surplusResource.min = 0
    surplusResource.max = None


def craft_calc(item: Item, levels, items):
    """ The main crafting algorithm

        Args:
            item (Item): The item to craft with the resources needed.
            levels ()
    """
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

        if (neededResource.average() > 0):
            resource = itemsDict.get(neededResource.name)

            if (resource is None):
                level = best[neededResource.name]
                run_level(find_level(level.level, levels), item, math.ceil(neededResource.min / level.average))

    print("")

    print(item)

    print("Redistributing surplus resources...\n")

    # Anything that's a surplus (a negative amount),  convert it to a resource that uses it.

    for resource in item.resources:
        if (resource.min < 0):
            itemWithNeededResource = find_item_with_needed_resource(resource.name, items)

            if (itemWithNeededResource is not None):
                convert_resource(itemWithNeededResource, resource, item)

    print(item)

    for neededResource in item.resources:
        level = best[neededResource.name]
        print(f"{round(neededResource.min):>4} {neededResource.name:<6} run level {level.level:<6} {math.ceil(neededResource.min / level.average):>3} times")

    print("")

    # TODO: Keep a list of "runs" then print them out at the end.

    print("\n")

    return None


def find_item_with_needed_resource(name: str, items):
    """ Find the item from the list with a resource that is needed.

        Args:
            name (str): The name of the resource to find.

        Returns:
            (Item):
    """
    for item in items:
        for resource in item.resources:
            if (resource.name == name):
                return item

    return None


def find_level(name: str, levels):
    """ Find a level from the list by name.

        Args:
            name (str): The name of the resource to find.
            levels (): The array of levels to search.

        Returns:
            (Level): Why WOULDN'T you want to know this from the function definition?  NOT ALLOWED IN PYTHON!!
    """
    for level in levels:
        if (level.name == name):
            return level

    return None


def run_level(level, item, count: int):
    """ Run a level many times and update an item's resources.

        Args:
            level ():
            item ():
            count (int):
    """

    print(f"Running Level '{level.name}' {count} times...")

    for resource in level.resources:
        item.add_to_resource(resource.name, count * -resource.average())