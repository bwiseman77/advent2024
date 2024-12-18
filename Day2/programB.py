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
        line = list(map(int, line.split()))
        if check_line(line):
            safe += 1
        else:
            # brute force check
            for i in range(0, len(line)):
                if check_line(line[:i] + line[i+1:]):
                    safe += 1
                    break
    print(safe)
if __name__ == "__main__":
    main()
