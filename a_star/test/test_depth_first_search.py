import random
import unittest

from depth_first_search import depth_first_search
from sliding_tile_problem import SlidingTileProblem
from sliding_tile_state import SlidingTileState


class TestDepthFirstSearch(unittest.TestCase):
    def test_one_tile_move(self):
        state = SlidingTileState(i=3, j=3)
        state.move(state.RIGHT)

        problem = SlidingTileProblem(initial_state=state)
        
        stats = depth_first_search(problem=problem)
        self.assertEqual(stats[0], [SlidingTileState.LEFT])

    def test_hardest_puzzle_instance(self):
        state = SlidingTileState(i=3, j=3, state=[8, 7, 6, 0, 4, 1, 2, 5, 3])
        problem = SlidingTileProblem(initial_state=state)
        
        solution, expanded, generated  = depth_first_search(problem=problem)
        print("%s %s" % (expanded, generated))

        self.assertTrue(len(solution) >= 31)

