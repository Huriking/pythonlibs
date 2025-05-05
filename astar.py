import heapq

def a_star_search(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, [start]))
    visited = set()

    while open_list:
        f, g, current_node, path = heapq.heappop(open_list)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            print("Goal node is reached:")
            print(f"Path is: {'->'.join(path)}")
            print(f"Total cost: {g}")
            return

        for neighbour, cost in graph.get(current_node, []):
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbour]
                heapq.heappush(open_list, (new_f, new_g, neighbour, path + [neighbour]))

    print("No path was found")
    return

def graph_input():
    graph = {}
    nodes = input("Please enter the nodes: ").split()

    print("Please enter the edges in format A B 3 (type 'done' to finish):")
    while True:
        line = input()
        if line.lower() == "done":
            break
        a, b, cost = line.split()
        cost = int(cost)
        graph.setdefault(a, []).append((b, cost))

    heuristics = {}
    print("Enter the heuristics for each node:")
    for node in nodes:
        h = input(f"h({node}) = ")
        heuristics[node] = int(h)

    return graph, heuristics

graph, heuristics = graph_input()
start = input("Enter starting node: ")
goal = input("Enter the goal node: ")
a_star_search(graph, heuristics, start, goal)
