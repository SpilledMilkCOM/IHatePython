class Game:

    def __init__(self, actions, midpoint):
        self.actions = actions
        self.rank = 0
        self.midpoint = midpoint

    def append(self, action):
        self.actions.append(action)

    def calc_rank(self ,a: int, b: int, c: int):
        # The 'values' field is a tuple
        for action in self.actions:
            a += action.values[0]
            b += action.values[1]
            c += action.values[2]

        self.rank = abs(a - self.midpoint) + abs(b - self.midpoint) + abs(c - self.midpoint)
