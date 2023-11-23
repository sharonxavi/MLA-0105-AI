import random

def objective_function(x):
    return -x**2 + 10  

def hill_climbing():
    current_solution = random.uniform(-10, 10) 
    current_value = objective_function(current_solution)

    while True:
        neighbor = current_solution + random.uniform(-1, 1)  
        neighbor_value = objective_function(neighbor)

        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value
        else:
            break 

    return current_solution, current_value

best_solution, best_value = hill_climbing()
print(f"Best solution found: x = {best_solution}, value = {best_value}")
