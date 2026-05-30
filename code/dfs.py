graph = {
    'A': ['B', 'C', 'D'],
    'D': ['E', 'F'],
    'B': ['H'],
    'C': [],
    'E': [],
    'F': [],
    'H': []
}

stack = ['A']
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

        for next_node in reversed(graph[current]):
            stack.append(next_node)

print("DFS Traversal:", visited)