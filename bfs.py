from collections import deque

def bfs_search(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            print(f"Path found: {' -> '.join(path)}")
            print(f"Number of steps: {len(path) - 1}")
            return path

        for neighbor, _ in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    print("No path found.")
    return None

def get_graph_input():
    graph = {}
    nodes = input("Enter all node names (space separated): ").split()

    while True:
        line = input()
        if line.lower() == "done":
            break
        a, b, cost = line.split()
        graph.setdefault(a, []).append((b, int(cost)))
        graph.setdefault(b, []).append((a, int(cost)))

    return graph

graph = get_graph_input()
start = input("Enter start node: ")
goal = input("Enter goal node: ")
bfs_search(graph, start, goal)
