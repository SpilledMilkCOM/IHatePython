import json

from crafting.item import Item
from crafting.resource import Resource

def create_warrior():
    resources = []
    resources.append(Resource("Water", 100))
    resources.append(Resource("Metal", 10))
    resources.append(Resource("Bone", 25))

    result = Item("He-Man", resources)

    return result

def create_warrior_from_json(data):

    # loads() only creates a data object (dict - no methods)
    # In complex objects you will get a dict of dicts

    warriorData = Item(**json.loads(data))

    # Build out the objects from the JSON data object.

    resources = []

    for resource in warriorData.resources:
        resources.append(Resource(resource['name'], resource['count']))

    # Instanciate the top level using the 

    return Item(warriorData.name, resources)

def dict_to_item(dict):

    # This feels like a hack, because the deserialization is based on known field names.
    # And if a Resource also had the field "resources" in it, then this would fail.

    resources = dict.get('resources')

    if resources is None:
        return Resource(dict['name'], dict['count'])
    else:
        return Item(dict['name'], resources)


def create_warrior_from_json2(data):

    return json.loads(data, object_hook=dict_to_item)