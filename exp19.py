import math
import random

def objective_function(x):
    return x**2 - 5*x + 6  

def simulated_annealing():
    current_state = random.uniform(-10, 10)  
    temperature = 1000  
    min_temperature = 0.1  
    cooling_rate = 0.95  

    while temperature > min_temperature:
        new_state = current_state + random.uniform(-1, 1)  
        current_cost = objective_function(current_state)
        new_cost = objective_function(new_state)

        delta_cost = new_cost - current_cost
        if delta_cost < 0 or random.uniform(0, 1) < math.exp(-delta_cost / temperature):
            current_state = new_state

        temperature *= cooling_rate  

    return current_state

best_solution = simulated_annealing()
min_value = objective_function(best_solution)
print(f"Best solution found: x = {best_solution}, value = {min_value}")
