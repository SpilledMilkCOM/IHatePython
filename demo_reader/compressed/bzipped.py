import bz2

# note the use of relatvie pathing
from ..util import writer

opener = bz2.open

if __name__ == '__main__':
    writer.main(opener)