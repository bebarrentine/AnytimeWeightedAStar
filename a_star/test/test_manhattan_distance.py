import unittest

from heuristics import manhattan_distance_8, manhattan_distance_15
from sliding_tile_state import SlidingTileState


class TestManhattanDistance(unittest.TestCase):
    def setUp(self):
        self.state = SlidingTileState(i=3, j=3)
        self.state15 = SlidingTileState(i=4, j=4, state=[
            3, 5, 10, 14, 7, 4, 15, 9, 13, 0, 8, 2, 12, 1, 6, 11
        ])

    def test_goal_state(self):
        self.assertEqual(manhattan_distance_8(state=self.state), 0)

    def test_one_tile_moved(self):
        self.state.move(self.state.RIGHT)
        self.assertEqual(manhattan_distance_8(state=self.state), 1)

    def test_manhattan_15(self):
        self.assertEqual(manhattan_distance_15(state=self.state15), \
            3 + 3 + 3 + 1 + 1 + 2 + 3 + 2 + 3 + 2 + 1 + 0 + 2 + 4 + 3
        )

