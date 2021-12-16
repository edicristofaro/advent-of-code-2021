from pprint import pprint

with open("input.txt", "r") as f:
    input = f.read().strip().split("\n")

points = {}
for i, l in enumerate(input):
    for j, c in enumerate(l):
        if int(c):
            points[(j, i)] = int(c)
        end = (j, i)

def adjacent_nodes(g, p):
    x, y = p
    # nodes = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    nodes = [(x + 1, y), (x, y + 1)]
    nodes = [n for n in nodes if n in g]

    return nodes # [n for n in g if n in nodes]

graph = {}
for p in points:
    graph[p] = adjacent_nodes(points, p)

start = (0,0)
queue = [start]
visited = { start: None }
path = []
print(f"Start: {start}, End: {end}")

while queue:
    node = queue.pop(0)
    # print(node)
    if node == end:
        path = []
        while node is not None:
            path.append(node)
            node = visited[node]
        break
    for n in graph[node]:
        if n not in visited:
            visited[n] = node
            queue.append(n)

print([points[p] for p in path])
print(sum(points[p] for p in path))