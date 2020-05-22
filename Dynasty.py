# import Decisions # You will have to prefix the commands in this file. (ex: Decisions.processCommand(command))

from Decisions import processCommand

from Models.GameState import GameState
from Models.Assets import Assets

def getCommand(gameCounter: int):
    """Allows the gamer to enter a command from the console."""
    return input("Dynasty (" + str(gameCounter) + ") > ")

def main():
    command = None
    gameState = GameState(Assets(100.0, 10, 10, 10))
    quit = False

    welcome()

    while not quit:
        command = getCommand(gameState.turnCount)

        if command == "q":
            quit = True

        processCommand(command)

        gameState.turnCount += 1    # NO ++

    print("\nCONGRATULATIONS! You lasted " + str(gameState.turnCount) + " rounds.\n")

def welcome():
    print("\nWelcome to Dynasty!\n")

welcome.__doc__ = "A friendly welcome to the game. (probably not the most preferred way to do this)"

main()
