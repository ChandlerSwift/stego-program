#!/usr/bin/env python3
# usage: stego.py input.bmp output.bmp [binary data to encode]
import sys

INPUT = open(sys.argv[1], "rb")
OUTPUT = open(sys.argv[2], "wb")
message = sys.argv[3]  # a binary message

img_header = INPUT.read(54)  # skip/don't modify the header
image = INPUT.read()

padded_msg = message + "1" + "0" * (len(image) - len(message) - 1)

stego_msg = map(lambda byte, bit: (byte & ~1) | int(bit), image, padded_msg)

OUTPUT.write(img_header + bytes(stego_msg))
