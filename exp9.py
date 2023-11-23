import itertools

def calculate_total_distance(path, distances):
    total_distance = 0
    num_cities = len(path)
    for i in range(num_cities - 1):
        total_distance += distances[path[i]][path[i + 1]]
    total_distance += distances[path[-1]][path[0]]  
    return total_distance

def traveling_salesman(cities, distances):
    num_cities = len(cities)
    shortest_distance = float('inf')
    shortest_path = None

    all_permutations = itertools.permutations(range(num_cities))

    for perm in all_permutations:
        current_distance = calculate_total_distance(perm, distances)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = perm

    return shortest_path, shortest_distance

cities = ["City A", "City B", "City C"]
distances = [
    [0, 10, 15],
    [10, 0, 20],
    [15, 20, 0]
]

shortest_path, shortest_distance = traveling_salesman(cities, distances)
print("Shortest Path:", shortest_path)
print("Shortest Distance:", shortest_distance)
