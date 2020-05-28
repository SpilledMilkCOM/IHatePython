import sys

def printXY(n: int):
    """Prints a string comprised of all combinations of X and Y up to width N."""

    if n < 0:
        raise ValueError("ERROR: n must be greater than or equal to 0")

    for i in range(2 ** n):
        print(f"{i:b}".replace("0", "X").replace("1", "Y"))

if __name__ == "__main__":
    printXY(int(sys.argv[1]))