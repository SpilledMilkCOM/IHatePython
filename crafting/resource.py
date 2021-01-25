class Resource(object):

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def to_string(self):
        return f"Resource: {self.name} x {self.count}"