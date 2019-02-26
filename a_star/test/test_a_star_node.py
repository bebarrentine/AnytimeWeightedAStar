import unittest

from a_star_node import AStarNode


class TestAStarNode(unittest.TestCase):
    def test_less_than_override(self):
        node = AStarNode(
            parent=None,
            path_cost=0,
            state=None,
            action=None,
            heuristic=lambda x: 0
        )

        other = AStarNode(
            parent=None,
            path_cost=1,
            state=None,
            action=None,
            heuristic=lambda x: 0
        )

        self.assertTrue(node < other)

