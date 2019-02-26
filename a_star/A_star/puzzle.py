# puzzle.py
# Contains definitions for classes and functions specific to sliding tile puzzles
import math
import random
import sys

WIDTH = 0
SIZE = 0
HEURISTIC = ""


def settings_init(width, size, heuristic):
    global WIDTH, SIZE, HEURISTIC
    WIDTH = width
    SIZE = size
    HEURISTIC = heuristic


class State:
    def __init__(self, board, parent, h=float('inf')):
        self.board = board
        self.parent = parent
        if parent is not None:
            self.c = parent.c + 1
        else:
            self.c = 0
        self.h = h
        self.hash = None

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        if self.hash is None:
            self.hash = hash(tuple(self.board))
        return self.hash

    def __str__(self):
        return " ".join(["_" if x == 0 else str(x) for x in self.board])

 
    #  Calculate manhanttan distance of current state
    def manhattan(self):
        self.h = 0

        for i in range(0, SIZE):
            self_index = i  # index on board
            goal_index = self.board[i] - 1  # corresponding index on goal board
            if goal_index == -1:  # don't calculate distance for 0
                continue

            dx = abs((self_index % WIDTH) - (goal_index % WIDTH))
            dy = abs((self_index // WIDTH) - (goal_index // WIDTH))
            self.h += dx + dy

   

    def calculate_h(self):
        try:
            if HEURISTIC == "manhattan":
                self.manhattan()
            else:
                raise ValueError("Invalid heuristic chosen")
        except ValueError as err:
            print(err)
            sys.exit(1)

    # Algorithm from https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
    def is_solvable(self):
        inversions = 0
        blank_row = None
        for i in range(SIZE):
            if self.board[i] == 0:
                blank_row = i // WIDTH
                continue
            for j in range(i, SIZE):
                if self.board[j] == 0:
                    continue

                if self.board[i] > self.board[j]:
                    inversions += 1

        if (WIDTH % 2 == 1) and (inversions % 2 == 1):
            return False
        elif (WIDTH % 2 == 0) and (blank_row % 2 == 1) and (inversions % 2 == 1):
            return False
        elif (WIDTH % 2 == 0) and (blank_row % 2 == 0) and (inversions % 2 == 0):
            return False
        else:
            return True


# Generate new state from current state
def move_right(state):
    tmp = state.board[:]
    i = tmp.index(0)
    if i % WIDTH != WIDTH - 1:
        tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
        return State(tmp, state)
    raise ValueError('invalid move right of state', tmp)


def move_left(state):
    tmp = state.board[:]
    i = tmp.index(0)
    if i % WIDTH != 0:
        tmp[i], tmp[i - 1] = tmp[i - 1], tmp[i]
        return State(tmp, state)
    raise ValueError('invalid move left of state', tmp)


def move_up(state):
    tmp = state.board[:]
    i = tmp.index(0)
    if i > WIDTH - 1:
        tmp[i], tmp[i - WIDTH] = tmp[i - WIDTH], tmp[i]
        return State(tmp, state)
    raise ValueError('invalid move up of state', tmp)


def move_down(state):
    tmp = state.board[:]
    i = tmp.index(0)
    if i < SIZE - WIDTH:
        tmp[i], tmp[i + WIDTH] = tmp[i + WIDTH], tmp[i]
        return State(tmp, state)
    raise ValueError('invalid move down of state', tmp)
