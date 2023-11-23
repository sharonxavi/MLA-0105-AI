from queue import PriorityQueue

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def calculate_heuristic(self):
        misplaced_tiles = sum([1 if self.state[i] != i + 1 else 0 for i in range(8)])
        return misplaced_tiles

def get_blank_index(state):
    return state.index(0)

def get_neighbors(node):
    neighbors = []
    blank_index = get_blank_index(node.state)
    row, col = divmod(blank_index, 3)

    possible_actions = [
        ('up', -3), ('down', 3), ('left', -1), ('right', 1)
    ]

    for action, offset in possible_actions:
        new_row, new_col = row + offset // 3, col + offset % 3
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = list(node.state)
            new_state[blank_index], new_state[new_row * 3 + new_col] = new_state[new_row * 3 + new_col], new_state[blank_index]
            neighbors.append(PuzzleNode(new_state, node, action, node.cost + 1))

    return neighbors

def solve_8_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    goal_state = list(range(1, 9)) + [0]
    goal_node = PuzzleNode(goal_state)

    frontier = PriorityQueue()
    frontier.put(initial_node)
    explored = set()

    while not frontier.empty():
        current_node = frontier.get()

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append((current_node.action, current_node.state))
                current_node = current_node.parent
            return list(reversed(path))

        explored.add(tuple(current_node.state))

        for neighbor in get_neighbors(current_node):
            if tuple(neighbor.state) not in explored:
                frontier.put(neighbor)

    return None  

def print_solution(path):
    for action, state in path:
        print(f"Action: {action}\n{state[0:3]}\n{state[3:6]}\n{state[6:9]}\n")

if __name__ == "__main__":
    initial_state = [1, 0, 3, 4, 2, 5, 7, 8, 6]
    solution_path = solve_8_puzzle(initial_state)

    if solution_path:
        print_solution(solution_path)
    else:
        print("No solution found.")

