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

    print("\n\n")

    return None