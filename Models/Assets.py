class Assets:
    """
    A class that contains all of the gamer's "stuff".
    (do you put the constructor param descriptions here?)
    """

    # Constructor / Definition

    def __init__(self, wealth: float, land: int, crops: int, people: int):
        """
        Args:
            wealth (float): Amount of money
            land (int): Acres of land
            crops (int): Amount of food
            people (int): Number of people
        """
        self.crops = crops
        self.land = land
        self.people = people
        self.wealth = wealth
