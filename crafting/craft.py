import sys

from mockUtil import createWarrior

def main(a: int, b: int, c: int):
    """Given A, B, and C - print the best actions to take to reduce the distance away from the midpoint
    
    Args:
        a (int): Once of the starting values
        b (int): Once of the starting values
        c (int): Once of the starting values
    """
    print(f"\n\nInputs: {a}, {b}, {c}\n")

    warrior = createWarrior()

    print(warrior.to_string())

if (__name__ == '__main__'):
    if (len(sys.argv) < 2):
        main(4, 5, 5)
    else:
        main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
