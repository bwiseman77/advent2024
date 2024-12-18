#! /usr/bin/env python3

import sys
import re

def count(line):

    # parse muls(X,Y)
    r = r'mul\(([0-9]+),([0-9]+)\)'
    res = re.findall(r, line)

    # get nums
    total = 0
    for x, y in res:
        print(x, y)
        total += (int(x) * int(y))

    # return result
    return total

def main():

    total = 0
    while line := sys.stdin.readline():
        total += count(line)

    print(total)
if __name__ == "__main__":
    main()
