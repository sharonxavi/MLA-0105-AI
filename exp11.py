import heapq

graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'D': 7, 'E': 12},
    'C': {'F': 6},
    'D': {'G': 8},
    'E': {'H': 9},
    'F': {'I': 11},
    'G': {},
    'H': {},
    'I': {}
}

heuristics = {
    'A': 15,
    'B': 10,
    'C': 8,
    'D': 6,
    'E': 7,
    'F': 8,
    'G': 3,
    'H': 5,
    'I': 0
}

def astar(graph, start, goal, heuristics):
    if start not in graph or goal not in graph:
        return None

    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0 + heuristics[start], 0, start))
    while priority_queue:
        _, cost, current_node = heapq.heappop(priority_queue)
        if current_node == goal:
            return visited

        visited.add(current_node)

        for neighbor, neighbor_cost in graph[current_node].items():
            if neighbor not in visited:
                total_cost = cost + neighbor_cost
                heapq.heappush(priority_queue, (total_cost + heuristics[neighbor], total_cost, neighbor))

    return None

start_node = 'A'
goal_node = 'I'
result = astar(graph, start_node, goal_node, heuristics)

if result:
    print(f"Path from {start_node} to {goal_node} found using A*: {list(result)}")
else:
    print(f"Path from {start_node} to {goal_node} not found.")
