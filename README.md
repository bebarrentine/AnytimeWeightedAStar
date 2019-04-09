# AnytimeWeightedAStar
Assignment for Dr. Hansen's Artificial Intelligence class (CSE 4633). Used listed algorithim to solve generated 8/15 square puzzles.

## Description of Algorithim:
Unlike A*, Anytime Weighted A* continues to search for a solution even after the first solution is found. This entails
Anytime Weighted A* requires more node expansions, and while this is true, Anytime Weighted
A* can still find a solution path faster than its A* counterpart. Due to its use of a weighted
heuristic, Anytime Weighted A* expands more distinct nodes compared to A*. Furthermore, a
weighted heuristic is also inconsitent which implies when a node is expanded it is possible for its
g-cost to be higher than optimal. Since A* is consistent, an expanded node cannot have a
higher-than-optimal g-cost putting it at a greater disability when compared to Anytime Weighted
A*. Anytime Weighted A*also employs the use of a lower-bound function and an upper bound
on the solution cost. Used together, they prune the search space and locate the convergence to an
ideal solution.
  
  
  
## Built With
* [Pycharm](https://www.jetbrains.com/pycharm/) - IDE used for creation and final testing
