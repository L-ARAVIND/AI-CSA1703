# Q10: A* Algorithm

from queue import PriorityQueue

def aStar(graph, start, goal, h):
    open_list = PriorityQueue()
    open_list.put((0, start))
    g = {node: float('inf') for node in graph}
    g[start] = 0
    parent = {start: None}

    while not open_list.empty():
        _, current = open_list.get()
        if current == goal:
            break
        for neighbor, cost in graph[current].items():
            temp = g[current] + cost
            if temp < g[neighbor]:
                g[neighbor] = temp
                f = temp + h[neighbor]
                open_list.put((f, neighbor))
                parent[neighbor] = current

    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path, g[goal]

graph = {
    'A': {'B':1, 'C':3},
    'B': {'A':1, 'D':1, 'E':5},
    'C': {'A':3, 'F':2},
    'D': {'B':1},
    'E': {'B':5, 'F':2},
    'F': {'C':2, 'E':2}
}
h = {'A':7,'B':6,'C':2,'D':1,'E':0,'F':3}
print("Path and cost:", aStar(graph, 'A', 'E', h))
