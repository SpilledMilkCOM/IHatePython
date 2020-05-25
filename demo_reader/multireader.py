# demo_reader/multireader.py

import os

from demo_reader.compressed import bzipped, gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener,
}

class MultiReader:
    def __init__(self, filename):
        self.filename = filename

        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        
        self._f = open(opener, mode='rt')

    def close(self):
        self._f.close()

    def read(self):
        return self._f.read()