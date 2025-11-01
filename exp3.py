def water_jug_problem(jug1, jug2, target):
    visited = set()
    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(x, y)
        if x == target or y == target:
            return True
        stack.extend([
            (jug1, y), (x, jug2), (0, y), (x, 0),
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ])
    return False

a, b, c = map(int, input("Enter Jug1, Jug2, and Target: ").split())
if not water_jug_problem(a, b, c):
    print("Not possible")
