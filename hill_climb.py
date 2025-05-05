import math
import random

cities = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (2, 3),
    'D': (4, 2),
    'E': (5, 5)
}

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_distance(route):
    dist = 0
    for i in range(len(route)):
        if i == len(route) - 1:
            dist += distance(route[i], route[0])
        else:
            dist += distance(route[i], route[i + 1])
    return dist

def get_neighbours(route):
    neighbours = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            new_route = route[:]  # Create a new copy each time
            new_route[i], new_route[j] = new_route[j], new_route[i]
            neighbours.append(new_route)
    return neighbours

def hill_climb(cities_list, max_iterations=20):
    current_soln = cities_list[:]
    random.shuffle(current_soln)
    current_cost = total_distance(current_soln)
    print(f"Initial solution: {current_soln} \nInitial Cost: {current_cost:.2f}")

    for i in range(max_iterations):
        neighbours = get_neighbours(current_soln)
        neighbour_distances = [(total_distance(n), n) for n in neighbours]
        best_neighbour = min(neighbour_distances, key=lambda x: x[0])

        if best_neighbour[0] < current_cost:
            current_cost = best_neighbour[0]
            current_soln = best_neighbour[1]
            print(f"{i + 1}. Improved Solution is {current_soln} and cost is {current_cost:.2f}")
        else:
            print("No Improvement")
            break

    print(f"Final solution is {current_soln} and cost is {current_cost:.2f}")
    return

hill_climb(list(cities.keys()), max_iterations=15)
