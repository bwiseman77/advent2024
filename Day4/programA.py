#! /usr/bin/env python3

import sys
from typing import List

XMAS = "XMAS"
MASX = "SAMX"

def read_grid() -> List[List[str]]:
    """  read in the grid """

    grid = []
    while line := sys.stdin.readline():
        grid.append(line.strip())

    return grid

def check_grid(grid: List[List[str]]) -> int:
    """ checks the grid for XMAS """

    count = 0
    # check rows
    for row in range(len(grid)):
        count += check_row(grid[row])

    # check cols
    for col in range(len(grid[0])):
        count += check_col(grid, col)

    # check diags
    for row in range(len(grid) - 3):
        for col in range(len(grid[0]) - 3):
            count += check_diag(grid, row, col)
    return count

def check_row(row: str) -> int:
    """ check 'row' for word """
    return row.count(XMAS) + row.count(MASX)

def check_col(grid: List[List[str]], col: int) -> int:
    """ check col for word """

    # convert a col to a row
    col = ''.join([grid[i][col] for i in range(len(grid[0]))])
    return check_row(col)

def check_diag(grid: List[List[str]], row: int, col: int) -> int:
    """ check a diag """
    diag1 = "".join([
            grid[row][col],
            grid[row+1][col+1],
            grid[row+2][col+2],
            grid[row+3][col+3]])

    diag2 = "".join([
            grid[row+3][col],
            grid[row+2][col+1],
            grid[row+1][col+2],
            grid[row][col+3]])

    return check_row(diag1) + check_row(diag2)

def check_x_mas(grid: List[List[str]]) -> int:
    """ checks for xmas """

    WORDS = ("MAS","SAM")

    total = 0
    for row in range(len(grid) - 2):
        for col in range(len(grid[0]) - 2):
            x1 = "".join([
                grid[row][col],
                grid[row+1][col+1],
                grid[row+2][col+2]])

            x2 = "".join([
                grid[row+2][col],
                grid[row+1][col+1],
                grid[row][col+2]])

            if x1 in WORDS and x2 in WORDS:
                total += 1

    return total

def main():
    grid = read_grid()
    print(check_grid(grid))
    print(check_x_mas(grid))

if __name__ == "__main__":
    main()
