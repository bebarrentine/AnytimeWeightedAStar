import copy
import unittest

from sliding_tile_problem import SlidingTileProblem
from sliding_tile_state import SlidingTileState
from action import Action



class TestSlidingTileProblem(unittest.TestCase):
    def setUp(self):
        state = SlidingTileState(i=3, j=3)
        self.problem = SlidingTileProblem(initial_state=state)

    def test_goal_test(self):
        state = SlidingTileState(i=3, j=3)

        self.assertTrue(self.problem.goal_test(state=state))


    def test_path_cost(self):
        path = (
            (
                SlidingTileState(i=3, j=3),
                Action(),
                SlidingTileState(i=3, j=3)
            ),
            (
                SlidingTileState(i=3, j=3),
                Action(),
                SlidingTileState(i=3, j=3)
            )
        )

        cost = self.problem.path_cost(path)

        self.assertEqual(cost, 2)

    def test_actions(self):
        state = SlidingTileState(i=3, j=3)
        actions = self.problem.actions(state)
        self.assertEqual(len(actions), 2)

        state.move(state.RIGHT)
        actions = self.problem.actions(state)
        self.assertEqual(len(actions), 3)

        state.move(state.DOWN)
        actions = self.problem.actions(state)
        self.assertEqual(len(actions), 4)

    def test_result(self):
        goal_state = SlidingTileState(i=3, j=3)
        goal_state.move(goal_state.RIGHT)

        state = self.problem.result(
            state=SlidingTileState(i=3, j=3),
            action=SlidingTileState.RIGHT
        )

        self.assertEqual(goal_state, state)

    def test_setting_initial_state(self):
        self.assertEqual(
            self.problem.initial_state, SlidingTileState(i=3, j=3)
        )


    def test_step_cost(self):
        state = copy.deepcopy(self.problem.initial_state)\
                    .move(SlidingTileState.RIGHT)

        self.assertEqual(
            self.problem.step_cost(
                from_state=self.problem.initial_state,
                action=SlidingTileState.RIGHT,
                to_state=state
            ),
            1
        )

