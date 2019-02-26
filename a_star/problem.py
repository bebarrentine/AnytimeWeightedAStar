class Problem:
    """Base class for implementing a problem for a search algorithm."""

    def __init__(self, initial_state=None):
        """Construct a new `Problem` object.

        Keyword arguments:
        - `initial_state`: The starting state of the problem.
        """
        self.initial_state = initial_state

    def actions(self, state=None):
        """Returns a list of all actions that can be taken in `state`.
        
        Keyword arguments:
        - `state`: The state to examine for possible actions.
        """

        return []

    def goal_test(self, state=None):
        """Always returns `True` in the base class.

        Keyword arguments:
        - `state`:
        """
        return True

    def result(self, state=None, action=None):
        """Returns None.

        When implemented, it returns the state that results from taking
        `action` in `state`.
        
        Keyword arguments:
        - `state`: The environment that `action` is taken in.
        - `action`: The act to take in `state`.
        """
        return None

    def path_cost(self, path=[]):
        """Returns the sum of the step costs between each node in the path."""
        return len(path)

