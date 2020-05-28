import sys

def print_xy(n: int):
    """Prints a string comprised of all combinations of X and Y of length N.
    
    Args:
        n (int): The width of the string
    """

    if n < 0:
        raise ValueError("ERROR: n must be greater than or equal to 0")

    format_spec = f"0{n}b"          # Need leading zeros to include all combinations

    for i in range(2 ** n):
        print(format(i, format_spec).replace("0", "X").replace("1", "Y"))

if __name__ == "__main__":
    print_xy(int(sys.argv[1]))