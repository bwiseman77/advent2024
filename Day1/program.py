#! /usr/bin/env python3

import sys

def main():


    list1, list2 = [], []
    while line := sys.stdin.readline():
        l = line.split()
        list1.append(int(l[0]))
        list2.append(int(l[1]))

    list1.sort()
    list2.sort()


    total = 0
    for a, b in zip(list1, list2):
        t = a - b

        total += t if t > 0 else -1 * t

    print(total)

if __name__ == "__main__":
    main()
