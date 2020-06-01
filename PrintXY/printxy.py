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


def print_xyx(n: int, digits: [str]):
    """Prints a string comprised of all combinations of the supplied digits of length N.
    
    Args:
        n (int): The width of the string
        digits ([str]): The characters to use as digits
    """

    if n < 0:
        raise ValueError("ERROR: n must be greater than or equal to 0")

    if digits is None:
        raise ValueError("ERROR: digits is None")

    base = len(digits)

    for i in range(base ** n):
        num_string = gen_string(i, base, digits)

        print((digits[0] * (n - len(num_string))) + num_string)


def gen_string(i: int, base: int, digits: [str]):
    """Returns a string representation of an integer given the list of digits.

    Args:
        i (int): The integer to generate
        base (int): The base representation of the number. (based on the length of the list)
        digits (int): The list of digits to use.
    """
    num_string = ""
    while i > 0:
        # Prepend the digit
        num_string = digits[i % base] + num_string
        # Effectively right shifting the number (dividing by the base)
        i //= base

    return num_string


if __name__ == "__main__":
    # print_xy(int(sys.argv[1]))
    # print_xyx(int(sys.argv[1]), ["X", "Y"])
    print_xyx(int(sys.argv[1]), ["X", "Y", "Z"])