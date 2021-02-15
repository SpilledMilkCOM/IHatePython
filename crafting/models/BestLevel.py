class BestLevel(object):

    def __init__(self, level: str, resource: str, unit: float, average: int):
        self.level = level
        self.resource = resource
        self.unit = unit
        self.average = average

    def __repr__(self):
        """ This is more for debugging and "evaluating" variables (versus converting them to a string)
            A video suggested that returning how the object was constructed might be best (or accepted in the community)
        """
        return f"{self.__class__.__name__}(\"{self.level}\", \"{self.resource}\", {self.unit}, {self.average})"

    def __str__(self):
        """ This is like the "ToString()" method in C#
            (Keep the readable formatting, because you can always strip it out later.)
        """
        return f"{self.__class__.__name__}: {self.level:<6} in {self.resource:<6} @ {self.unit:.3f} / unit"