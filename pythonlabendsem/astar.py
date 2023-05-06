import heapq

def heuristic(n, goal):
    H_dist = { 'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0}
    return H_dist[n]

def astar(graph, start, goal):
    visited = {}
    heap = [(0, start, [])]
    heapq.heapify(heap)
    cost_so_far = {start: 0}
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        if node == goal:
            return path + [node], cost_so_far[goal]
        if node in visited:
            continue
        visited[node] = True
        for neighbor, weight in graph[node].items():
            new_cost = cost_so_far[node] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(heap, (new_cost + heuristic(neighbor, goal), neighbor, path + [node]))
    return None, None

start_node = 'A'
goal_node = 'J'

Graph_nodes = {
    'A': {'B': 6, 'F': 3},
    'B': {'C': 3, 'D': 2},
    'C': {'E': 5},
    'D': {'C': 1, 'E': 8},
    'E': {'J': 5},
    'F': {'G': 1, 'H': 7},
    'G': {'I': 3},
    'H': {'I': 2},
    'I': {'E': 5, 'J': 3},
}

path, cost = astar(Graph_nodes, start_node, goal_node)

if path is None:
    print("No path found")
else:
    print("Minimum cost path:", path)
    print("Cost of the path:", cost)
