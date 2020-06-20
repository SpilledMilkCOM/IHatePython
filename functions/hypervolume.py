def hypervolume(*lengths):
    i = iter(lengths)       # Positional arguments are passed in as a tuple
    v = next(i)
    for length in i:
        v *= length
    return v
