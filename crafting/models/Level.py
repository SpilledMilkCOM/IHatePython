import json

from models.Resource import Resource

class Level:

    def __init__(self, name = None, cost: int = None, resources = None):
        self.name = name
        self.cost = cost
        self.resources = resources

    def deserialize(self, data: str):

        # !! There has GOT to be a more generic way to deserialize objects !!

        return json.loads(data, object_hook=Level().dict_to_item)

    def dict_to_item(self, dict):

        # This feels like a hack, because the deserialization is based on known field names.
        # And if a Resource also had the field "resources" in it, then this would fail.

        resources = dict.get("resources")

        if resources is None:
            name = dict.get("name")
            min = dict.get("min")
            max = dict.get("max")

            # How do you break up logical statements onto different lines?

            if name is None and min is None and max is None:
                return None
            else:
                return Resource(name, min, max)
        else:
            return Level(dict["name"], dict["energy"], resources)

    def to_string(self):
        result = f"Level: {self.name}\n\tCost: {self.cost}\n"

        for resource in self.resources:
            result += f"\t{resource.to_string()}\n"

        return result