"""The Decisions module contains the command parsing logic."""

validCommands = ["h", "w"]

def processCommand(command: str):
    # NOTE: that type hinting is still used above
    """Processes the gamer's input.

    (below is the Google docstrings example)
    
    Args:
        command (str): The command to process
    """
    
    print("User entered : " + command)