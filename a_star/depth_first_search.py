from collections import deque
from node import Node


def depth_first_search(problem=None):
    grey = 0
    black = 1
    state_space = {}
    expanded = 0

    queue = deque([Node(
        state=problem.initial_state,
        path_cost=0,
        parent=None
    )])
    queue[0].color = grey
    generated = 1

    while queue:
        node = queue.popleft()
        node.color = black

        actions = problem.actions(node.state)

        for action in actions:
            child_state = problem.result(action=action, state=node.state)

            try:
                if node.parent.parent.state == child_state:
                    continue
            except:
                None

            step_cost = problem.step_cost(
                from_state=node.state,
                action=action,
                to_state=child_state
            )

            child_node = Node(
                parent=node,
                state=child_state,
                path_cost=node.path_cost + step_cost,
                action=action
            )
            generated = generated + 1

            if not(child_node.state in state_space):
                if problem.goal_test(child_node.state):
                    solution = []
                    node = child_node

                    try:
                        while node.action:
                            solution.append(node.action)
                            node = node.parent
                    except:
                        None

                    solution.reverse()
                    return (solution, generated, expanded)
                else:
                    queue.appendleft(child_node)
                    child_node.color = grey
                    state_space[child_node.state] = child_node
                    expanded = expanded + 1

    return (None, expanded, generated)
            
