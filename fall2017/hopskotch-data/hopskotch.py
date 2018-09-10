#!/usr/bin/env python3
# Title: Solver for the "Hopskotch" puzzle I came up with for CS@Mines
# Puzzle Challenge
# Author: Jack Rosenthal
# Date: 2017-07-16
# Usage: python3 hopskotch <hopskotch.in
import sys
from string import ascii_uppercase as alpha
from collections import defaultdict, deque


def nodename(row, col):
    """The human readable node name: e.g., (0, 0) -> A1"""
    res = ''
    while True:
        res = alpha[row % 26] + res
        row //= 26
        if not row:
            break
    return res + str(col + 1)


# First, read the puzzle from stdin, creating an augmented graph
G = defaultdict(list)
rows = int(input())
cols = int(input())
finish = (rows - 1, cols - 1)
for r in range(rows):
    row = [int(x) for x in input().split()]
    for c in range(cols):
        for pos in ((r, c + row[c]), (r, c - row[c]),
                    (r + row[c], c), (r - row[c], c)):
            if 0 <= pos[0] < rows and 0 <= pos[1] < cols and pos != (r, c):
                G[(r, c)].append(pos)


# Yay, BFS!
Q = deque([(0, 0)])
path = {}
while Q:
    node = Q.pop()
    if node == finish:
        # Solved!
        break
    for adj in G[node]:
        if adj not in path.keys():
            path[adj] = node
            Q.appendleft(adj)
else:
    print("Maze has no solution.")
    sys.exit(1)

# Traceback!
pos = finish
sol = []
while pos != (0, 0):
    sol.append(pos)
    pos = path[pos]
sol.append(pos)

# Show the solution!
print("Solution:", *(nodename(*n) for n in reversed(sol)))
