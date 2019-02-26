from node import Node


class AStarNode(Node):
    """Provides a node framework for A* graph search.

    Using the `Node` class works for breadth-first search and depth-first
    search, but since A* requires a computation of the f-cost of a node, we
    have to subclass it.

    Keyword arguments:
    - `heuristic`: A reference to a heuristic function that takes a `State` as
      a single argument, and returns an estimate of the distance from the
      goal.
    """

    def __init__(self, *args, **kwargs):
        super(AStarNode, self).__init__(*args, **kwargs)
        self.heuristic = kwargs["heuristic"]

        self.weight = 1.2  # created self.weight and assigned 1.2 as value ------------

    def unweightH(self):  # added unweightH (H standing for heuristic) ------------
        return self.path_cost + self.heuristic(self.state)

    def __lt__(self, other):
        """Returns `True` if `self`'s f-cost is lower than `other`'s."""
        # "It is well-known that A* achieves best performance when it breaks
        # ties in favor of nodes with the least h-cost." [1]
        try:
            if self.f_cost < other.f_cost:
                return True
            elif self.f_cost == other.f_cost:
                return self.h < other.h
            else:
                return False
        # If an f-cost hasn't been calculated for a node, then make sure they
        # both have f-costs before comparing.
        except AttributeError:
            if not hasattr(self, "f_cost"):
                self.h = self.heuristic(self.state)
                self.f_cost = self.path_cost + self.h * self.weight  # multiplied heuristic by self.weight ------------

            if not hasattr(other, "f_cost"):
                other.h = other.heuristic(other.state)
                other.f_cost = other.path_cost + other.h * self.weight  # multiplied heuristic by self.weight ------------

        return self.__lt__(other)

    def __gt__(self, other):
        """Returns `True` if `self`'s f-cost is greater than `other`'s.
        
        Overriding `>` is easy if you reverse the terms and flip the
        inequality the other way to `<`. That way, we only have one operator
        to override.
        """
        return other < self

# [1] Hansen, E. and Zhao R., "Anytime Heuristic Search", Journal of
#     Artificial Intelligence Research 28 (2007) 267-297, March 2007.
