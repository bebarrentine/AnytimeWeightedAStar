# The Manhattan distance heuristic for a sliding tile puzzle estimates the
# number of remaining moves a sliding tile puzzle needs to reach the goal
# state.
#
# Each tile's distance is computed by summing the number of horizontal and
# vertical moves needed to move the tile to its place in the goal state.
#
# Given a goal state:
#
#     +---+---+---+
#     |   | 1 | 2 |
#     +---+---+---+
#     | 3 | 4 | 5 |
#     +---+---+---+
#     | 6 | 7 |*8*|
#     +---+---+---+
#
# If tile 8 is in posiion (2, 2), and the number of rows _n_ = 3,
# then dividing the tile's value by the number of rows in the
# puzzle reveals its current row.
#
#     8 // 3 == 2. # Integer division, drop the fraction.
#     
# If the tile's current row _i_ is subtracted, then the absolute
# value of the difference is the vertical distance from its place
# in the goal state:
#
#     (tile  // n) - i
#     (8 // (3)) - (2) == 0
#
#vertical_distance = abs(tile // state.get_num_rows() - i)
## The tile's value mod the number of columns in the puzzle
## reveals its column in the goal state. Then its current column
## is subtracted, and the absolute value of this difference reveals
## the distance from its place in the goal state.
#horizontal_distance = abs((tile % state.get_num_cols()) - j)
## Sum the manhattan distance of all tiles in the current state of
## the puzzle.
#distance = distance + vertical_distance + horizontal_distance
#
#  return distance

manhat8 = []
def init_8():
    """Compute every distance for each tile position in the 8 puzzle."""
    for tile in range(9):
        manhat8.append([])

        for i in range(3):
            for j in range(3):
                position = i * 3 + j

                distance = 0
                # Don't do any computations for the blank.
                if 0 < tile:
                    # From Richard Korf's A* implementation.
                    distance = abs(tile % 3 - position % 3) \
                        + abs(tile // 3 - position // 3)

                manhat8[tile].append(distance)
    return
init_8()

manhat15 = []
def init_15():
    """Compute every distance for each tile position in the 8 puzzle."""
    for tile in range(16):
        manhat15.append([])

        for position in range(16):
            distance = 0
            if 0 < tile:
                distance = abs((tile % 4) - (position % 4)) \
                    + abs((tile // 4) - (position // 4))

            manhat15[tile].append(distance)
    return
init_15()

def manhattan_distance_8(state=None):
    """Estimates a 3x3 sliding tile puzzle's distance from the goal state.
    
    Keyword arguments:
    - `state`: An object of type `Puzzle`. For this assignment, a
      `SlidingTileState` instance will be passed here.

    Returns: sum of those distances.
    """

    sum = 0

    for i in range(3):
        for j in range(3):
            sum = sum + manhat8[state.tile_at(i, j)][i * 3 + j]

    return sum


def manhattan_distance_15(state=None):
    """Estimates a 4x4 sliding tile puzzle's distance from the goal state.
    
    Keyword arguments:
    - `state`: An object of type `Puzzle`. For this assignment, a
      `SlidingTileState` instance will be passed here.

    Returns: sum of those distances.
    """

    sum = 0

    for i in range(4):
        for j in range(4):
            sum = sum + manhat15[state.tile_at(i, j)][i * 4 + j]

    return sum

