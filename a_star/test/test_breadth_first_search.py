import random
import unittest

from breadth_first_search import breadth_first_search
from sliding_tile_problem import SlidingTileProblem
from sliding_tile_state import SlidingTileState


class TestBreadthFirstSearch(unittest.TestCase):
    def test_one_tile_move(self):
        state = SlidingTileState(i=3, j=3)
        state.move(state.RIGHT)

        problem = SlidingTileProblem(initial_state=state)
        
        stats = breadth_first_search(problem=problem)
        self.assertEqual(stats[0], [SlidingTileState.LEFT])

    def test_hardest_puzzle_instance(self):
        state = SlidingTileState(i=3, j=3, state=[8, 7, 6, 0, 4, 1, 2, 5, 3])
        problem = SlidingTileProblem(initial_state=state)
        
        solution, expanded, generated = breadth_first_search(problem=problem)
        print("%s %s" % (expanded, generated))

        self.assertEqual(len(solution), 31)

    def test_random_puzzle_instance(self):
        state = SlidingTileState(i=3, j=3)
        problem = SlidingTileProblem(initial_state=state)

        num_moves = 50
        for i in range(num_moves):
            action = random.randint(1, 5)

            while not state.can_move(action):
                action = random.randint(1, 5)

            state.move(action)
        
        solution, expanded, generated = breadth_first_search(problem=problem)

        self.assertTrue(num_moves >= len(solution))

