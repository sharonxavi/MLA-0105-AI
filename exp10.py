from queue import PriorityQueue

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

def best_first_search(graph, start, goal):
    if start not in graph or goal not in graph:
        return None

    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))

    while not priority_queue.empty():
        cost, current_node = priority_queue.get()
        visited.add(current_node)

        if current_node == goal:
            return visited

        for neighbor, neighbor_cost in graph[current_node].items():
            if neighbor not in visited:
                priority_queue.put((neighbor_cost, neighbor))

    return None

start_node = 'A'
goal_node = 'I'
result = best_first_search(graph, start_node, goal_node)

if result:
    print(f"Path from {start_node} to {goal_node} found using Best First Search: {list(result)}")
else:
    print(f"Path from {start_node} to {goal_node} not found.")
