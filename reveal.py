#!/usr/bin/env python3
import sys

INPUT = open(sys.argv[1], "rb")

data = INPUT.read()
decoded = ""
for byte in data:
    decoded += str(byte & 1)
decoded = decoded.rstrip("0")[:-1]  # remove zero padding
print(decoded)
