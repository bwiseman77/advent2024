#! /usr/bin/env python3

import sys
import re

DONT    = "don't()"
DO      = "do()"
ENABLED = True

def count(line):

    global ENABLED

    # parse muls(X,Y) and do(nt)s
    r = r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)'
    res = re.findall(r, line)

    # pop thru stack 
    total = 0
    for inst in res:
        if inst == DONT:
            ENABLED = False
        elif inst == DO:
            ENABLED = True
        else:
            if ENABLED:
                x, y = re.findall(r'mul\(([0-9]+),([0-9]+)\)', inst)[0]
                total += int(x) * int(y)

    return total

def main():

    total = 0
    while line := sys.stdin.readline():
        total += count(line)

    print(total)
if __name__ == "__main__":
    main()
