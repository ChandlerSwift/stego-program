# Bitmap Steganography Demo
Created by Chandler Swift for MATH 5347 at University of Minnesota Duluth

`stego.py` is a program written to demonstrate simple encoding of binary data
in a bitmap file. `reveal.py` reverses the process and prints the encoded data
from a file that has been encoded with `stego.py`.

This method of encoding encodes 1 bit per byte of bitmap data, so in the given
example of the 6 megabyte image of trees, 6 megabits, or about 768KB could be
stored.

### Usage
Encoding: `python3 stego.py <input.bmp> <output.bmp> <binary data>`
Decoding: `python3 reveal.py <input.bmp>`

### Examples
The original image (from /r/EarthPorn: https://redd.it/7d2u0m):

[![trees.bmp](/examples/trees-thumb.jpg?raw=true)](/examples/trees.bmp)

The image encoded with binary 42 (`101010`):

[![trees.bmp](/examples/trees-thumb.jpg?raw=true)](/examples/trees-message.bmp)

The image with all least-significant-bits turned to ones:

[![trees.bmp](/examples/trees-thumb.jpg?raw=true)](/examples/trees-ones.bmp)

The image with all least-significant-bits turned to zeros:

[![trees.bmp](/examples/trees-thumb.jpg?raw=true)](/examples/trees-zeros.bmp)

Note that all the images are indistinguishable. The last two should be the
theoretically most different. Note that because the last two are not padded
they are not decodable by stego.py.
