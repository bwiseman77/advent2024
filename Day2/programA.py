#! /usr/bin/env python3

import sys

SAFE = (-3, -2, -1, 1, 2, 3)

def check_line(line):
    delta = 0
    for i in range(1, len(line)):

        d = line[i-1] - line[i]
        # check range
        if d not in SAFE:
            return False

        # check inc/dec
        elif delta == 0:
            delta = d
        else:
            if delta * d < 0:
                return False

    return True


def main():

    safe = 0
    while line := sys.stdin.readline():
        if(check_line(list(map(int, line.split())))):
            safe += 1

    print(safe)
if __name__ == "__main__":
    main()
