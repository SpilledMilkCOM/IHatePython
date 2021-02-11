import json

from models.Item import Item
from models.Level import Level
from models.Resource import Resource

def create_warrior():
    resources = []
    resources.append(Resource("Water", 100))
    resources.append(Resource("Metal", 10))
    resources.append(Resource("Bone", 25))

    result = Item("He-Man", resources)

    return result

def create_warrior_from_json2(data):

    # loads() only creates a data object (dict - no methods)
    # In complex objects you will get a dict of dicts

    warriorData = Item(**json.loads(data))

    # Build out the objects from the JSON data object.

    resources = []

    for resource in warriorData.resources:
        resources.append(Resource(resource['name'], resource['count']))

    # Instanciate the top level using the 

    return Item(warriorData.name, resources)

    
def create_levels_from_json(data: str):
    # Constructs an Level() to use the method/hook
    return Level().deserialize(data)


def create_warrior_from_json(data: str):
    # Constructs an Item() to use the method/hook
    return Item().deserialize(data)

def print_mock_warrior():
    warrior = create_warrior()

    print(warrior.to_string())

    print(json.dumps(warrior, default=lambda childObj: childObj.__dict__, indent=4))

    # Alphabetical fields
    # print(json.dumps(warrior, default=lambda childObj: childObj.__dict__, indent=4, sort_keys=True))

    data = json.dumps(warrior, default=lambda childObj: childObj.__dict__)

    warrior = create_warrior_from_json2(data)

    print(warrior.to_string())