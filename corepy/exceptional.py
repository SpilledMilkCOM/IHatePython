import sys

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def convert(s):
    """Convert a string to an integer"""

    x = -1
    number = ''

    try:
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)

    except (KeyError, TypeError) as ex:       # A tuple of exception types.
        # pass        # Ignore the exception - A noop since empty blocks are not acceptable in Python.

        print(f"Conversion error: {ex!r}", file=sys.stderr)

    return x