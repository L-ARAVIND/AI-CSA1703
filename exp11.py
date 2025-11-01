

colors = ['Red', 'Green', 'Blue']
regions = {
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E'],
    'E':['C','D']
}

def assign(region, assignment):
    for color in colors:
        conflict = any(assignment.get(neigh) == color for neigh in regions[region])
        if not conflict:
            yield color

def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment
    region = [r for r in regions if r not in assignment][0]
    for color in assign(region, assignment):
        assignment[region] = color
        result = backtrack(assignment)
        if result: return result
        del assignment[region]
    return None

print("Solution:", backtrack({}))
