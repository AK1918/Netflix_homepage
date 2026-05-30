graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 4},
    'C': {'D': 1},
    'D': {}
}

h = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 0
}

start = 'A'
goal = 'D'

open_list = [start]
visited = []

g_cost = {
    'A': 0
}

while open_list:

    current = open_list[0]

    for node in open_list:

        current_f = g_cost[current] + h[current]
        node_f = g_cost[node] + h[node]

        if node_f < current_f:
            current = node

    open_list.remove(current)

    if current not in visited:
        visited.append(current)

    if current == goal:
        break

    for next_node in graph[current]:

        if next_node not in open_list and next_node not in visited:

            open_list.append(next_node)

            g_cost[next_node] = (
                g_cost[current]
                + graph[current][next_node]
            )

print("Visited Nodes:", visited)
print("Total Cost:", g_cost[goal])