from puzzle import Puzzle
from state import State


class SlidingTileState(Puzzle, State):
    """The state to use for the sliding tile problem.

    A `SlidingTileState` is both a `Puzzle` and a `State`, making search much
    easier since the same methods for a `Puzzle` can be used for a
    `SlidingTileState`.
    """

    None

