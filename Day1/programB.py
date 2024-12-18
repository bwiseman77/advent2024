#! /usr/bin/env python3

import sys

def main():

    # read input
    list1, list2 = [], []
    while line := sys.stdin.readline():
        l = line.split()
        list1.append(int(l[0]))
        list2.append(int(l[1]))

    # build counts
    counts = {}
    for number in list2:
        counts[number] = counts.get(number, 0) + 1

    # get score 
    score = 0
    for number in list1:
        if number in counts:
            score += counts[number] * number

    print(score)
if __name__ == "__main__":
    main()
