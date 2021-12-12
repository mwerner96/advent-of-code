import networkx as nx


def visit(node='start', visited=set()):
    if node == 'end':
        return 1
    if node in visited:
        return 0
    v = visited.copy()
    if node.islower():
        v.add(node)
    sum = 0
    for child in caves[node]:
        sum += visit(child, v)
    return sum


with open('input') as f:
    caves = nx.Graph([tuple(l.strip().split('-')) for l in f.readlines()])

print(visit())
