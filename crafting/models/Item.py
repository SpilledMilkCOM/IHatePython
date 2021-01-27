import json

from models.Resource import Resource

class Item(object):

    def __init__(self, name: str = None, resources = None):
        self.name = name
        self.resources = resources

    def deserialize(self, data: str):

        # !! There has GOT to be a more generic way to deserialize objects !!

        return json.loads(data, object_hook=Item().dict_to_item)

    def dict_to_item(self, dict):

        # This feels like a hack, because the deserialization is based on known field names.
        # And if a Resource also had the field "resources" in it, then this would fail.

        resources = dict.get("resources")

        if resources is None:
            name = dict.get("name")
            count = dict.get("count")

            if name is None and count is None:
                return None
            else:
                return Resource(name, count)
        else:
            return Item(dict["name"], resources)

    def __str__(self):
        """ This is like the "ToString()" method in C#
        """
        result = f"Item: {self.name}\n"

        for resource in self.resources:
            result += f"\t{resource}\n"

        return result