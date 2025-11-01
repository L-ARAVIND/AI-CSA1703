from collections import deque

def is_valid(state):
    m_left, c_left, boat = state
    m_right, c_right = 3 - m_left, 3 - c_left
    if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
        return False
    return 0 <= m_left <= 3 and 0 <= c_left <= 3

def successors(state):
    m, c, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    res = []
    for dm, dc in moves:
        if boat == 1:
            new = (m - dm, c - dc, 0)
        else:
            new = (m + dm, c + dc, 1)
        if is_valid(new):
            res.append(new)
    return res

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for s in successors(state):
            if s not in visited:
                visited.add(s)
                queue.append((s, path + [s]))
    return None

path = bfs((3,3,1),(0,0,0))
print("Solution Path:", path)
