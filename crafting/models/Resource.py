class Resource(object):

    def __init__(self, name: str, min: int, max: int = None):
        self.name = name
        self.min = min
        self.max = max

    def __str__(self):
        """ This is like the "ToString()" method in C#
        """
        if self.max is None:
            return f"Resource: {self.name} x {self.min}"
        else:
            return f"Resource: {self.name} x ({self.min}-{self.max})"