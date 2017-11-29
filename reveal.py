#!/usr/bin/env python3
import sys

INPUT = open(sys.argv[1], "rb")

decoded = ""
for byte in INPUT.read():
    decoded += str(byte & 1)  # Strip the trailing bit from each byte
decoded = decoded.rstrip("0")[54:-1]  # skip header; remove padding
print(decoded)
