class State:
    def __init__(self, jugs):
        self.jugs = jugs
        
    def __eq__(self, other):
        return self.jugs == other.jugs
    
    def __hash__(self):
        return hash(tuple(self.jugs))
    
    def __str__(self):
        return str(self.jugs)
    
class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        
    def __str__(self):
        return str(self.state)

def get_successors(state, jug_sizes):
    successors = []
    a, b = state.jugs
    size_a, size_b = jug_sizes
    # Fill jug a
    successors.append((State((size_a, b)), f'fill {size_a}-gallon jug'))
    # Fill jug b
    successors.append((State((a, size_b)), f'fill {size_b}-gallon jug'))
    # Pour from jug a to jug b
    amount = min(a, size_b-b)
    successors.append((State((a-amount, b+amount)), f'pour from {size_a}-gallon jug to {size_b}-gallon jug'))
    # Pour from jug b to jug a
    amount = min(b, size_a-a)
    successors.append((State((a+amount, b-amount)), f'pour from {size_b}-gallon jug to {size_a}-gallon jug'))
    # Empty jug a
    successors.append((State((0, b)), f'empty {size_a}-gallon jug'))
    # Empty jug b
    successors.append((State((a, 0)), f'empty {size_b}-gallon jug'))
    return successors

def dfs(node, goal_state, explored, jug_sizes):
    if node.state == goal_state:
        actions = []
        while node.parent is not None:
            actions.append(node.action)
            node = node.parent
        actions.reverse()
        return actions
    explored.add(node.state)
    for successor, action in get_successors(node.state, jug_sizes):
        child_node = Node(successor, node, action)
        if child_node.state not in explored:
            result = dfs(child_node, goal_state, explored, jug_sizes)
            if result is not None:
                return result
    return None

jug_sizes = (5, 3)
initial_state = State((0, 0))
goal_state = State((4, 0))
initial_node = Node(initial_state)
explored = set()
actions = dfs(initial_node, goal_state, explored, jug_sizes)
if actions is None:
    print('No solution found.')
else:
    print('Solution found in', len(actions), 'steps:')
    for action in actions:
        print(action)
