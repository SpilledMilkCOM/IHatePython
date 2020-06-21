import sys

from action import Action
from game import Game

# All of the available actions that can be taken
actions = [
    Action(1, (3, 0, -1))
    , Action(2, (-3, -2, 3))
    , Action(3, (2, 0, -2))
    , Action(4, (-2, 2, 0))
    , Action(5, (0, -3, 2))
    , Action(6, (0, 3, - 2))
]

midpoint = 8
numActions = 5
games = []          # The result set


def main(a: int, b: int, c: int):
    """Given A, B, and C - print the best actions to take to reduce the distance away from the midpoint
    
    Args:
        a (int): Once of the starting values
        b (int): Once of the starting values
        c (int): Once of the starting values
    """
    print(f"Inputs: {a}, {b}, {c}\n")

    for action in actions:
        mainActions = [ action ]
        generate(mainActions, numActions - 1)

    print("Total possibilities:" + str(len(games)))

    for game in games:
        game.calc_rank(a, b, c)

    games.sort(reverse=False, key=lambda game: game.rank)

    for game in games[0:10]:
        print(f"\n{game.rank}")
        for action in game.actions:
            print(action.number, action.values)

def generate(currentActions: [], level: int):
    """A recursive function that will append the actions at the base level
    
    Args:
        currentActions ([Action]): The list of actions
        level (int): The current level
    """
    if (level == 0):
        games.append(Game(currentActions, midpoint))
    else:
        for action in actions:
            actionsCopy = currentActions.copy()
            actionsCopy.append(action)
            generate(actionsCopy, level - 1)


if (__name__ == '__main__'):
    if (len(sys.argv) < 2):
        main(4, 5, 5)
    else:
        main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
