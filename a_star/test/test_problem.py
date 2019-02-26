import unittest


from action import Action
from problem import Problem
from state import State


class TestProblem(unittest.TestCase):
    def setUp(self):
        self.problem = Problem()

    def test_goal_test(self):
        self.assertTrue(self.problem.goal_test(state=None))

    def test_result(self):
        self.assertEqual(self.problem.result(State(), Action()), None)

    def test_path_cost(self):
        self.assertEqual(self.problem.path_cost([]), 0)

    def test_initial_state(self):
        self.assertIsNone(self.problem.initial_state)

    def test_actions(self):
        self.assertIsInstance(self.problem.actions(State()), list)

