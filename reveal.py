#!/usr/bin/env python3
import sys

INPUT = open(sys.argv[1], "rb")

data = INPUT.read()
decoded = ""
for byte in data:
    decoded += str(byte & 1)
decoded = decoded.rstrip("0")[54:-1]  # skip header; remove padding
print(decoded)
