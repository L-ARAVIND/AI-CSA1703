

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("DFS Traversal:", dfs(graph, 'A'))
