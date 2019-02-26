import unittest
import random

from a_star import a_star
from heuristics import manhattan_distance_8, manhattan_distance_15
from problem import Problem
from sliding_tile_state import SlidingTileState
from sliding_tile_problem import SlidingTileProblem


class TestAStar(unittest.TestCase):

    # removed first test

    def test_one_tile_move(self):
        state = SlidingTileState(i=3, j=3)
        state.move(state.RIGHT)

        problem = SlidingTileProblem(initial_state=state)

        solution = a_star(problem=problem, heuristic=manhattan_distance_8)[0]
        self.assertEqual(solution, [SlidingTileState.LEFT])

    def test_random_puzzle(self):
        state = SlidingTileState(i=3, j=3)
        shuffle_puzzle(puzzle=state, num_moves=1000)

        problem = SlidingTileProblem(initial_state=state)

        solution = a_star(problem=problem, heuristic=manhattan_distance_8)[0]

        self.assertIsNotNone(solution)

        for action in solution:
            state.move(action)

        self.assertEqual(state.signature, 0x012345678)

    def test_puzzle_instance(self):
        state = SlidingTileState(i=3, j=3, state=[6, 4, 0, 8, 1, 3, 5, 7, 2])
        problem = SlidingTileProblem(initial_state=state)

        solution = a_star(problem=problem, heuristic=manhattan_distance_8)[0]

        self.assertEqual(len(solution), 22)

        for action in solution:
            state.move(action)

        self.assertEqual(state.signature, 0x012345678)

    def test_hardest_puzzle_instance(self):
        state = SlidingTileState(i=3, j=3, state=[8, 7, 6, 0, 4, 1, 2, 5, 3])
        problem = SlidingTileProblem(initial_state=state)

        solution, expanded, generated, reopened = a_star(
            problem=problem, heuristic=manhattan_distance_8
        )
        print("%s %s" % (expanded, generated))

        self.assertEqual(len(solution), 31)

    def test_other_hardest_puzzle_instance(self):
        state = SlidingTileState(i=3, j=3, state=[8, 0, 6, 5, 4, 7, 2, 3, 1])
        problem = SlidingTileProblem(initial_state=state)

        solution, expanded, generated, reopened = a_star(
            problem=problem, heuristic=manhattan_distance_8
        )
        print("%s %s" % (expanded, generated))

        self.assertEqual(len(solution), 31)

    def test_15_puzzle(self):
        state = SlidingTileState(i=4, j=4)
        shuffle_puzzle(state, 20)

        problem = SlidingTileProblem(initial_state=state)

        solution, expanded, generated, reopened = a_star(
            problem=problem, heuristic=manhattan_distance_15
        )

        while solution:
            state.move(solution.pop(0))

        self.assertTrue(problem.goal_test(state))


def shuffle_puzzle(puzzle=None, num_moves=0):
    previous_action = None
    for i in range(num_moves):
        action = generate_action(previous_action=previous_action)
        while not puzzle.can_move(action):
            action = generate_action(previous_action=previous_action)

        puzzle.move(action)
        previous_action = action


def generate_action(previous_action=None):
    action = random.randint(1, 5)
    is_reverse = is_reverse_of(action=action, previous_action=previous_action)

    while is_reverse:
        action = random.randint(1, 5)
        is_reverse = is_reverse_of(
            action=action, previous_action=previous_action
        )

    return action


def is_reverse_of(action=None, previous_action=None):
    is_reverse = False

    if SlidingTileState.UP == action and \
            SlidingTileState.DOWN == previous_action:
        is_reverse = True
    elif SlidingTileState.DOWN == action and \
            SlidingTileState.UP == previous_action:
        is_reverse = True
    elif SlidingTileState.LEFT == action and \
            SlidingTileState.RIGHT == previous_action:
        is_reverse = True
    elif SlidingTileState.RIGHT == action and \
            SlidingTileState.LEFT == previous_action:
        is_reverse = True

    return is_reverse


if __name__ == '__main__':  # implemented a main function so I could run the test
    unittest.main()
