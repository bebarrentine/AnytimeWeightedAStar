import copy

from problem import Problem
from sliding_tile_state import SlidingTileState


class SlidingTileProblem(Problem):
    """A sliding tile problem that is passed to search algorithms."""

    def __init__(self, initial_state=None):
        """Setup a sliding tile problem object.

        Keyword arguments:
        - `i`: The number of rows in this sliding tile problem.
        - `j`: The number of columns in this sliding tile problem.
        - `initial_state`: A `SlidingTileState` that represents the
          environment the search algorithm will start in.
        """
        # Setup `SlidingTileProblem` like a `Problem`.
        super().__init__(initial_state=initial_state)

        # Set the number of rows and columns for the problem.
        self.num_rows = self.initial_state.num_rows
        self.num_cols = self.initial_state.num_cols

        # Setup a goal state.
        self.goal = SlidingTileState(i=self.num_rows, j=self.num_cols)

        return

    def actions(self, state=None):
        """Returns a list of possible actions that can be taken in `state`.
        
        Keyword arguments:
        - `state`: The environment in which to consider the actions that can
          be taken.
        """
        # The list of actions to be returned.
        actions = []

        # Test each action to see if we can take it in `state`. If so, append
        # it to the `actions` list.
        if state.can_move(state.UP):
            actions.append(state.UP)

        if state.can_move(state.DOWN):
            actions.append(state.DOWN)

        if state.can_move(state.LEFT):
            actions.append(state.LEFT)

        if state.can_move(state.RIGHT):
            actions.append(state.RIGHT)

        return actions

    def goal_test(self, state=None):
        """Returns a boolean depending on `state` being a goal state.
        
        Keyword arguments:
        - `state`: The state to test to determine if it is a goal state.
        """
        return self.goal == state

    # `result` returns a `SlidingTileState` 
    def result(self, state=None, action=None):
        """Returns a new state that reflects taking `action` in `state`.
        
        Keyword arguments:
        - `state`: The environment that `action` is taken in.
        - `action`: The act to take in `state`.
        """
        # Make a copy of `state` to return.
        resulting_state = copy.copy(state)

        # Take `action` in `state`. Note that if the move cannot be done in
        # `state`, then `resulting_state` is unmodified.
        resulting_state.move(action)

        return resulting_state

    def step_cost(self, from_state=None, action=None, to_state=None):
        """Returns the cost of doing `action` in `from_state` to `to_state`.
        
        For the sliding tile puzzle, every swap has a step cost of 1. But if
        `action` is a null action, or `action` can't be taken in `from_state`,
        then the step cost is zero.
        """
        # If no action was passed, or we can't take `action` in `from_state`,
        # then the step cost is zero.
        if None == action or not from_state.can_move(action):
            return 0
        # If we can take the action, then the step cost is 1.
        else:
            return 1

