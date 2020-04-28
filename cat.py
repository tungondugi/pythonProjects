#!/usr/bin/python
"""Written by nognut"""
"""The following python script is the python equivalent for Linux/Unix command 'cat'."""
import sys
def cat(filename):
    with open(filename, 'r') as file:
        for e in file.readlines():
            print(e.rstrip())

if __name__ == "__main__":
    filename = sys.argv[1]
    cat(filename)
