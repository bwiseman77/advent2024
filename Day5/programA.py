#! /usr/bin/env python3
from functools import cmp_to_key


import sys

def read_input():
    """ build a map of ordering rules 
            page : [list of numbers that must be after] 
    """
    ordering = {}

    while line := sys.stdin.readline().strip():
        pages  = line.strip().split('|')

        if int(pages[0]) in ordering:
            ordering[int(pages[0])].add(int(pages[1]))
        else:
            ordering[int(pages[0])] = {int(pages[1])}

    return ordering

def run_updates(ordering, updates):
    """ check an update for correct ordering """
    seen = set()
    for update in updates:

        if update in ordering and ordering[update] & seen:
            return False

        seen.add(update)

    return True

def fix_updates(ordering, updates):
    # bubble sort swap (?)
    isBroken = True
    while isBroken:
        isBroken = False
        seen = [] # (val,idx)
        for i in range(len(updates)):
            if updates[i] in ordering:
                for s in seen:
                    if s[0] in ordering[updates[i]]:
                        isBroken = True
                        updates[i], updates[s[1]] = updates[s[1]], updates[i]

            seen.append((updates[i], i))


    return updates

# Main Execution

def main():

    # 1. get ordering
    ordering = read_input()

    # 2. find correct updates
    correct   = []
    incorrect = []
    while line := sys.stdin.readline():
        line = list(map(int, line.strip().split(',')))

        if run_updates(ordering, line):
            correct.append(line)
        else:
            incorrect.append(line)

    # 3. count middle values
    total = 0
    for update in correct:
        total += update[len(update)//2]

    print("Correct:", total)

    # 4. fix incorrect
    total = 0
    for updates in incorrect:
        fixed = fix_updates(ordering, updates)
        total += fixed[len(fixed)//2]
    print("Incorrect:", total)

if __name__ == "__main__":
    main()
