#!/usr/bin/env python3
import sys

INPUT = open(sys.argv[1], "rb")
OUTPUT = open(sys.argv[2], "wb")

data = INPUT.read(54)  # don't modify the header

data += bytes(map(lambda byte: (byte & ~1) | 0, INPUT.read()))

OUTPUT.write(data)
