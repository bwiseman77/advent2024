#! /usr/bin/env python3

import sys

# Globals

EDGE = '@'
OBJ  = '#'
STRT = '^'
DIRS = {
        'U' : 'R',
        'R' : 'D',
        'D' : 'L',
        'L' : 'U',
    }

# Functions

def read_map():
    """ Reads in the map from stdin """
    grid = []

    # read grid and add '@' barrier buffer
    while line := sys.stdin.readline():
        grid.append(['@'] + list(line.strip()) + ['@'])

    # add barrier on top and bottom
    grid.insert(0, ['@']*len(grid[0]))
    grid.append(['@']*len(grid[0]))

    return grid

def find_start(grid):
    """ returns the starting position """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == STRT:
                return (i, j, 'U')

def printg(grid):
    """ print the grid """
    for row in grid:
        print(row)

def next_pos(grid, pos):
    """ returns next pos """
    delta = pos[2]

    # find next spot
    if delta == 'U':
        n = (pos[0]-1, pos[1], delta)
    elif delta == 'R':
        n = (pos[0], pos[1]+1, delta)
    elif delta == 'D':
        n = (pos[0]+1, pos[1], delta)
    else: # delta == 'L':
        n = (pos[0], pos[1]-1, delta)

    # check for edge or obj
    if grid[n[0]][n[1]] == EDGE:
        return None

    if grid[n[0]][n[1]] == OBJ:
        return (pos[0], pos[1], DIRS[pos[2]])

    # return the pos
    return n

def patrol_r(grid, start):
    """ helper for pt2 to find loops """
    curr = start
    seen = set()
    while True:
        # some how check for loops
        if curr in seen:
            break

        seen.add(curr)

        pos = next_pos(grid, curr)

        # hit the edge
        if pos is None:
            return False

        curr = pos

    return True
def patrol(grid, start):
    """ make the guard patrol the grid from start """
    curr = start
    seen = set()
    objs = set()

    while True:
        seen.add((curr[0], curr[1]))
        pos = next_pos(grid, curr)

        # hit the edge
        if pos is None:
            return (len(seen), len(objs))

        # try add an obj before we move
        obj = (pos[0], pos[1])
        o = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = "#"
        if patrol_r(grid, start):
            #print("found loop w obj at:",obj)
            #printg(grid)
            objs.add(obj)

        grid[pos[0]][pos[1]] = o

        # move
        curr = pos

# Main Execution

def main():
    grid = read_map()
    start = find_start(grid)
    p1   = patrol(grid, start)

    print(p1)

if __name__ == "__main__":
    main()
