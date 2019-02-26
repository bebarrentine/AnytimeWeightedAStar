import copy
import heapq

from a_star_node import AStarNode


def a_star(problem=None, heuristic=None):
    expanded = generated = reopened = 0
    state_space = {}

    node = AStarNode(
        state=copy.deepcopy(problem.initial_state),
        parent=None,
        path_cost=0,
        action=None,
        heuristic=heuristic,
    )

    node.in_frontier = False
    generated = generated + 1

    frontier_pq = [node]
    state_space[node.state] = node
    node.in_frontier = True

    solution = None
    incumbent = None  # added incumbent ------------

    while frontier_pq:
        node = heapq.heappop(frontier_pq)
        node.in_frontier = False
        expanded = expanded + 1  # moved

        try:  # added ------------
            if incumbent is None or node.fcost < incumbent.fcost:  # changed goal ------------
                state_space[node.state] = node

                for action in problem.actions(node.state):

                    new_state = problem.result(state=node.state, action=action)

                    step_cost = problem.step_cost(
                        from_state=node.state,
                        action=action,
                        to_state=new_state
                    )

                    child_node = AStarNode(
                        state=new_state,
                        parent=node,
                        path_cost=node.path_cost + step_cost,
                        action=action,
                        heuristic=heuristic)

                    generated = generated + 1

                    try:  # added ------------
                        if child_node.unweightH() >= incumbent.unweightH():
                            continue
                    except Exception:
                        pass

                    in_frontier = child_node.state in state_space and \
                        state_space[child_node.state].in_frontier

                    in_explored = False
                    if not in_frontier:

                        if child_node.state in state_space and \
                                not state_space[child_node.state].in_frontier:
                            in_explored = True

                    if not in_explored and not in_frontier:
                        heapq.heappush(frontier_pq, child_node)
                        state_space[child_node.state] = child_node
                        child_node.in_frontier = True

                    if problem.goal_test(child_node.state):  # added ------------
                        incumbent = child_node

                    elif child_node.state in state_space:  # added ------------
                        if child_node.path_cost > node.path_cost:
                            state_space[child_node.state] = child_node
                            if in_explored:
                                heapq.heappush(frontier_pq, child_node)
                                child_node.in_frontier = True

                    elif in_frontier:
                        if state_space[child_node.state] > child_node:
                            state_space[child_node.state].path_cost = \
                                child_node.path_cost
                            state_space[child_node.state].parent = child_node.parent
                            state_space[child_node.state].action = child_node.action
                            state_space[child_node.state].f_cost = child_node.f_cost

                            heapq.heapify(frontier_pq)

                            reopened = reopened + 1

                    else:  # added ------------
                        child_node.in_frontier = True
                        state_space[child_node.state] = child_node
                        heapq.heappush(frontier_pq, child_node)
                        heapq.heapify(frontier_pq)

            state_space[node.state] = node

        except AttributeError:  # added ------------
            pass

    if problem.goal_test(incumbent.state):

        if incumbent.action:  # changed node to incumbent ------------
            solution = [incumbent.action]
            while incumbent:
                incumbent = incumbent.parent
                if incumbent and None is not incumbent.action:
                    solution.insert(0, incumbent.action)

    return solution, expanded, generated, reopened
