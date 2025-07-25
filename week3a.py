from sys import maxsize
from itertools import permutations

v = 4

def travellingSalesmanProblem(graph, s):
    vertex = []

    for i in range(v):
        if i != s:
            vertex.append(i)

    min_path = maxsize

    next_perm = permutations(vertex)

    for i in next_perm:
        print(i)
        current_pathweight = 0
        k = s
        for j in i:
            print(j)
            current_pathweight += graph[k][j]
            k = j

        current_pathweight += graph[k][s]
        min_path = min(current_pathweight,min_path)

    return min_path

graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

s = 0

print(travellingSalesmanProblem(graph, s))