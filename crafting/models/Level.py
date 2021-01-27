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

    def __repr__(self):
        """ This is more for debugging and "evaluating" variables (versus converting them to a string)
            A video suggested that returning how the object was constructed might be best (or accepted in the community)
        """
        first = True

        result = f"{self.__class__.__name__}(\"{self.name}\",{self.cost},\n\t[\n"

        for resource in self.resources:
            result += "\t"

            if not first:
                result += ","
            else:
                result += " "
                first = False

            result += f" {repr(resource)}\n"

        result += "\t]\n)"

        return result

    def __str__(self):
        """ This is like the "ToString()" method in C#
            (Keep the readable formatting, because you can always strip it out later.)
        """
        result = f"{self.__class__.__name__}: {self.name}\n\tCost: {self.cost}\n"

        for resource in self.resources:
            result += f"\t{resource}\n"

        return result