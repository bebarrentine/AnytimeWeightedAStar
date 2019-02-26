import unittest

from node import Node
from sliding_tile_state import SlidingTileState


class TestNode(unittest.TestCase):
    def setUp(self):
        self.state = SlidingTileState(i=3, j=3)
        self.parent = Node(
            path_cost=0, action=None, state=self.state, parent=None
        )
        self.action = 1
        self.path_cost = 3
        self.node = Node(
            action=self.action,
            path_cost=self.path_cost,
            parent=self.parent,
            state=self.state
        )

