graph = {
    'a' : ['b', 'c', 'd'],
    'b' : ['e', 'f'],
    'c' : [],
    'd' : ['g'],
    'e' : [],
    'f' : [],
    'g' : []
}

queue = ['a']
visited = []

while queue: 
    current = queue.pop(0)
    if current not in visited: 
        visited.append(current)
    
    for next_node in graph[current]:
        queue.append(next_node)
    
print("BFS traversal:", visited)