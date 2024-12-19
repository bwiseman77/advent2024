#! /usr/bin/env python3

import sys
from collections import defaultdict

# Globals

# Functions

def read_input():
    """ reads input and returns a mapping for antenna types : list of points """
    data = [list(line.strip()) for line in sys.stdin]

    mapping = defaultdict(list)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != '.':
                mapping[data[i][j]].append((i,j))

    return [mapping, len(data), len(data[0])]

def printd(data):
    """ just prints data """
    for d in data:
        print(d)

def product(items):
    """ yields cartisean product (unique)"""
    for A in items:
        for B in items:
            if A != B:
                yield (A,B)

def find_locations(mapping, ymax, xmax):
    """ finds locations of antinodes """
    locs = set()

    # go over each antenna type
    for antenna in mapping:
        # go thru each possible pair of points
        for pt1, pt2 in product(mapping[antenna]):

            # find distance between 2 points
            dx = pt1[1] - pt2[1]
            dy = pt1[0] - pt2[0]

            # extend past each point
            anti = (pt1[0]+dy,pt1[1]+dx)
            while 0 <= anti[0] < ymax and 0 <= anti[1] < xmax:
                locs.add(anti)
                anti = (anti[0]+dy, anti[1]+dx)

            anti = (pt2[0]-dy,pt2[1]-dx)
            while 0 <= anti[0] < ymax and 0 <= anti[1] < xmax:
                locs.add(anti)
                anti = (anti[0]-dy, anti[1]-dx)

    return len(locs)

# Main Execution

def main():
    mapping, ymax, xmax = read_input()
    ans = find_locations(mapping, ymax, xmax)
    print(ans)

if __name__ == "__main__":
    main()
