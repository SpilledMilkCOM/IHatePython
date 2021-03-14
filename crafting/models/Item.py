import json

from .Resource import Resource

class Item(object):

    def __init__(self, name: str = None, resources = None):
        self.name = name
        self.resources = resources

    def __add__(self, item):
        """ Overload of the "+" operator.
        """
        clone = self.clone()

        for resource in clone.resources:
            for itemResource in item.resources:
                if (resource.name == itemResource.name):
                    if (resource.max is not None and itemResource.max is not None):
                        resource.max += itemResource.max
                    resource.min += itemResource.min
                    break
 
        return clone

    def add_to_resource(self, name: str, amount: int):
        for resource in self.resources:
            if (resource.name == name):
                if (resource.max is None):
                    resource.min += amount
                else:
                    resource.min = (resource.min + resource.max) / 2 + amount
                    resource.max = None

    def clone(self):
        """ A deep clone of self.
        """
        clone = Item(self.name)

        clone.resources = []

        for resource in self.resources:
            clone.resources.append(resource.clone())

        return clone

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
    
    def __repr__(self):
        """ This is more for debugging and "evaluating" variables (versus converting them to a string)
            A video suggested that returning how the object was constructed might be best (or accepted in the community)
        """
        first = True

        result = f"{self.__class__.__name__}(\"{self.name}\",\n\t[\n"

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

    def resource(self, name: str):
        """ Lookup a needed resource by name.

          Args:
            name (str): The name of the resource to find.
        """
        for resource in self.resources:
            if (resource.name == name):
                return resource
        return None

    def __str__(self):
        """ This is like the "ToString()" method in C#
            (Keep the readable formatting, because you can always strip it out later.)
        """
        result = f"{self.__class__.__name__}: {self.name}\n"

        for resource in self.resources:
            result += f"\t{resource}\n"

        return result