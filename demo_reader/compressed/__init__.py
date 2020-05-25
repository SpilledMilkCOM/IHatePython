from demo_reader.compressed.bzipped import opener as bz2_opener
from demo_reader.compressed.gzipped import opener as gzip_opener

# If import * is ever used, ONLY export the following
__all__ = ['bz2_opener', 'gzip_opener']