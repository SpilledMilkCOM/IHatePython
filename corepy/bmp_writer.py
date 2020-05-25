"""A module for dealing with BMP image files."""

from int32_to_bytes import _int32_to_bytes

def write_grayscale(filename, pixels):
    """Craetes and writes a grayscale BMP file.

    Args:
        filename: The name of the BMP file to be created.

        pixels: A rectangular image stored as a sequence of rows.
            Each row must ben an iterable series of integers
            in the range of 0-255

    Raises:
        ValueError: If any of the integer values are out of range.
        OSError: If the file couldn't be written.
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        # BMP Header
        bmp.write(b'BM')

        # The next four bytes hold the file size as a 32-bit
        # little-endian integer. Zero placeholder for now.
        size_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')

        bmp.write(b'\x00\x00\x00\x00')  # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00\x00\x00')  # Unused 16-bit integer - should be zero

        # The next four bytes hold the integer offset to the
        # pixel data. Zero placeholder for now.
        pixel_offset_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')

        # Image Header
        bmp.write(b'\x28\x00\x00\x00')      # Image header size in bytes - 40 decimal
        bmp.write(_int32_to_bytes(width))   # Image width in pixels
        bmp.write(_int32_to_bytes(height))  # Image height in pixels
        bmp.write(b'\x00\x00\x00\x00')      # No compression
        bmp.write(b'\x00\x00\x00\x00')      # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')      # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')      # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')      # Use whole color table
        bmp.write(b'\x00\x00\x00\x00')      # All colors are important

        # Color palette - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))  # Blue, Green, Red, Zero (Alpha - opacity)

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):    # BMP files are bottom to top
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * ((4 - (len(row) % 4)) % 4)  # Pad row to multiple of four bytes
            bmp.write(padding)

        # End of file
        eof_bookmark = bmp.tell()

        # Fill infile size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))

