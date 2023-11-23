from collections import deque

def is_valid_state(state, jug1_capacity, jug2_capacity):
    jug1, jug2 = state
    return 0 <= jug1 <= jug1_capacity and 0 <= jug2 <= jug2_capacity

def get_next_states(current_state, jug1_capacity, jug2_capacity):
    jug1, jug2 = current_state
    all_states = set()
    
    all_states.add((jug1_capacity, jug2))
    
    all_states.add((jug1, jug2_capacity))
    
    all_states.add((0, jug2))
    
    all_states.add((jug1, 0))
    
    pour_amount = min(jug1, jug2_capacity - jug2)
    all_states.add((jug1 - pour_amount, jug2 + pour_amount))
    
    pour_amount = min(jug2, jug1_capacity - jug1)
    all_states.add((jug1 + pour_amount, jug2 - pour_amount))
    
    return [state for state in all_states if is_valid_state(state, jug1_capacity, jug2_capacity)]

def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    visited = set()
    queue = deque([(0, 0)])
    
    while queue:
        current_state = queue.popleft()
        if current_state[0] == target_amount or current_state[1] == target_amount:
            return current_state
        
        visited.add(current_state)
        next_states = get_next_states(current_state, jug1_capacity, jug2_capacity)
        
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
    
    return None

jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

solution = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
if solution:
    print(f"Target amount of {target_amount} liters achieved: {solution}")
else:
    print("Target amount cannot be achieved with the given jug capacities.")
