class Node:
    """Used in search algorithms to explore the state space.

    Parameters:
    - `action`: The action taken to arrive at `state`. `None` if this is a
      root node.
    - `parent`: The parent node of this node. `None` if this is a root node.
    - `path_cost`: The sum of every step cost from the root to this node.
    - `state`: An instance of a `State` class.
    """

    def __init__(
        self,
        parent=None,
        action=None,
        path_cost=None,
        state=None,
        **kwargs):

        self.state = state
        self.action = action
        self.parent = parent 
        self.path_cost = path_cost

    def __eq__(self, other):
        """Make it easier to compare nodes.

        Overriding the equality operator eases the search for nodes in the
        open and closed sets.
        """
        # States are the only attribute being compared.
        return self.state == other.state

