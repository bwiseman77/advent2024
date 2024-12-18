#! /usr/bin/env python3

import sys

# Globals

OPRS = ['*', '+']

# Functions

def solve(target, vals, curr, equ):

    # base cases
    if str(curr) == str(target) and len(vals) == 0:
        #print(equ+"="+str(target))
        return True

    if len(vals) == 0:
        return False

    # try * 
    if solve(target, vals[1:], curr*vals[0], equ+"*"+str(vals[0])):
        return True
    # try +
    if solve(target, vals[1:], curr+vals[0], equ+"+"+str(vals[0])):
        return True
    # try ||
    if solve(target, vals[1:], int(str(curr)+str(vals[0])), equ + str(vals[0])):
        return True

    return False

# Main Execution

def main():

    total = 0
    while line := sys.stdin.readline():
        line = line.split(':')
        target, vals = int(line[0]), list(map(int,line[1].split()))

        if solve(target, vals[1:], vals[0], str(vals[0])):
            total += target

    print(total)

if __name__ == "__main__":
    main()
