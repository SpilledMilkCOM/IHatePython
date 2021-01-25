class Item(object):

    def __init__(self, name, resources):
        self.name = name
        self.resources = resources

    def to_string(self):
        result = f"Item: {self.name}\n"

        for resource in self.resources:
            result += f"\t{resource.to_string()}\n"

        return result