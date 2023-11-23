from collections import deque

initial_state = (3, 3, 1)  
def is_valid(state):
    missionaries, cannibals, boat = state

    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False

    if missionaries > 0 and missionaries < cannibals:
        return False

    return True

def get_next_states(state):
    missionaries, cannibals, boat = state
    possible_states = []

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    if boat == 1: 
        for move in moves:
            new_state = (missionaries - move[0], cannibals - move[1], 0)
            if is_valid(new_state):
                possible_states.append(new_state)
    else:  
        for move in moves:
            new_state = (missionaries + move[0], cannibals + move[1], 1)
            if is_valid(new_state):
                possible_states.append(new_state)

    return possible_states

def bfs():
    queue = deque()
    visited = set()
    parent = {}

    queue.append(initial_state)
    visited.add(initial_state)
    parent[initial_state] = None

    while queue:
        current_state = queue.popleft()

        if current_state == (0, 0, 0):  
            solution_path = []
            while current_state:
                solution_path.append(current_state)
                current_state = parent[current_state]
            return solution_path[::-1] 

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)
                parent[next_state] = current_state

    return None 

def print_solution(solution):
    if solution:
        print("Missionaries and Cannibals Solution:")
        for state in solution:
            missionaries, cannibals, boat = state
            print(f"Left Bank: {missionaries} missionaries, {cannibals} cannibals | Boat Position: {'Left' if boat == 1 else 'Right'}")
    else:
        print("No solution found for the Missionaries and Cannibals problem.")

solution_path = bfs()
print_solution(solution_path)
