import copy
import sys

sys.setrecursionlimit(1500)

with open("input.txt", "r") as f:
    edges = [l.strip("\n") for l in f.readlines()]

nodes = []
n = [e.split("-") for e in edges]
for e in n:
    nodes.append(e[0])
    nodes.append(e[1])
nodes = list(set(nodes))

print(edges)
print(nodes)

i = 0
paths = []
visitable_nodes = copy.deepcopy(nodes)

# get start node
# find its neighbors using edges
# find the neighbors neighbors using edges
## if the starting node is lowercase, remove it from the visitable_nodes list passed to the function
# until no more visitable nodes

def is_uppercase(string):
    for s in string:
        if s.islower():
            return False
    return True
 
def find_neighbors(start, edges, visitable_nodes):
    visitable_nodes = copy.deepcopy(visitable_nodes)
    # print(edges)
    # edges = [e.split("-") for e in edges]
    print(start, visitable_nodes)
    if start == 'end':
        return [start]
    for e in edges:
        ee = e.split("-")
        if start in ee:
            if ee[0] == start and ee[1] in visitable_nodes:
                if not is_uppercase(start) and start in visitable_nodes:
                    visitable_nodes.remove(start)
                n = [start]
                n.append(find_neighbors(ee[1], edges, visitable_nodes))
                print("condition 1", n)
                return n
            elif ee[1] == start and ee[0] in visitable_nodes:
                if not is_uppercase(start) and start in visitable_nodes:
                    visitable_nodes.remove(start)
                n = [start]
                n.append(find_neighbors(ee[0], edges, visitable_nodes))
                print("condition 2", n)
                return n
        # return []
                

paths = []
print(paths.append(find_neighbors("start", edges, visitable_nodes)))

# below is cheating - i couldn't figure this one out
# looks like i needed to start my recursion one level deeper, and accumulate at the end

"""
def get_all_paths(graph,node,destination):
    visited = set()
    path = list()
    all_paths = list()
    def get_paths(graph, node,destination,visited,path):
        if node.islower():
            visited.add(node)
        path.append(node)

        if node == destination:
            all_paths.append(path.copy())
        else:
            for next_node in graph[node]:
                if next_node not in visited:
                    get_paths(graph, next_node, destination, visited, path)
        path.pop()
        if node.islower():
            visited.remove(node)


    get_paths(graph,node,destination,visited,path)

    return all_paths


def main():
    graph = dict()
    with open('input.txt','r') as infile:
        for line in infile.readlines():
            caveA,caveB = line.strip().split("-")
            if caveA in graph:
                graph[caveA].append(caveB)
            else:
                graph[caveA] = [caveB]
            if caveB in graph:
                graph[caveB].append(caveA)
            else:
                graph[caveB] = [caveA]

    all_paths = get_all_paths(graph, 'start','end')
    print(len(all_paths))



if __name__ == '__main__':
    main()


def get_all_paths(graph,node,destination,repeat_lower):
    visited = set()
    path = list()
    all_paths = list()
    repeat_visit = False
    def get_paths(graph, node,destination,visited,path, repeat_visit):
        if node in['start','end'] or (node.islower() and (node!=repeat_lower or repeat_visit == True)):
            visited.add(node)
        elif node == repeat_lower and repeat_visit == False:
            repeat_visit = True

        path.append(node)

        if node == destination:
            all_paths.append(path.copy())
        else:
            for next_node in graph[node]:
                if next_node not in visited:
                    get_paths(graph, next_node, destination, visited, path, repeat_visit)
        path.pop()
        if node in['start','end'] or (node.islower() and (node!=repeat_lower or repeat_visit == True)):
            if node not in visited:
                repeat_visit == False
            else:
                visited.remove(node)

    get_paths(graph,node,destination,visited,path, repeat_visit)

    return all_paths


def main():
    graph = dict()
    with open('input.txt','r') as infile:
        for line in infile.readlines():
            caveA,caveB = line.strip().split("-")
            if caveA in graph:
                graph[caveA].append(caveB)
            else:
                graph[caveA] = [caveB]
            if caveB in graph:
                graph[caveB].append(caveA)
            else:
                graph[caveB] = [caveA]

    lowers = {key for key in graph.keys() if key.islower()}

    all_paths = list()
    for lower in lowers:
        all_paths.extend(get_all_paths(graph, 'start','end',lower))

    all_paths = {tuple(path) for path in all_paths}
    print(len(all_paths))



if __name__ == '__main__':
    main()
"""