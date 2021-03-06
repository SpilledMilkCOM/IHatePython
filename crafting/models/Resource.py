class Resource(object):

    def __init__(self, name: str, min: int, max: int = None):
        self.name = name
        self.min = min
        self.max = max

    def __repr__(self):
        """ This is more for debugging and "evaluating" variables (versus converting them to a string)
            A video suggested that returning how the object was constructed might be best (or accepted in the community)
        """
        return f"{self.__class__.__name__}(\"{self.name}\", {self.min}, {self.max})"

    def __str__(self):
        """ This is like the "ToString()" method in C#
            (Keep the readable formatting, because you can always strip it out later.)
        """
        if self.max is None:
            return f"{self.__class__.__name__}: {self.name} x {self.min}"
        else:
            return f"{self.__class__.__name__}: {self.name} x ({self.min}-{self.max})"