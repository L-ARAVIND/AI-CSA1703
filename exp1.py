from collections import deque

def is_solvable(state):
    inv = 0
    nums = [int(x) for x in state if x != '0']
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                inv += 1
    return inv % 2 == 0

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    moves = {'U': -3, 'D': 3, 'L': -1, 'R': 1}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        visited.add(state)
        idx = state.index('0')
        for m, pos in moves.items():
            new_idx = idx + pos
            if 0 <= new_idx < 9:
                if (m == 'L' and idx % 3 == 0) or (m == 'R' and idx % 3 == 2):
                    continue
                new_state = list(state)
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                new_state = ''.join(new_state)
                if new_state not in visited:
                    queue.append((new_state, path + [m]))
    return None

start = input("Enter start state (e.g. 123405678): ")
goal = input("Enter goal state (e.g. 123456780): ")

if is_solvable(start):
    path = bfs(start, goal)
    print("Path to goal:", path)
else:
    print("This puzzle cannot be solved.")
