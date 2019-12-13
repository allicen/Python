import json

string = json.loads(input())
classes = {}
classesParents = {}

for i in string:
    classes.update({i["name"]: set(i["parents"])})


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


for i in classes:
    classesParents.update({i: bfs(classes, i)})

for k in sorted(classesParents.keys()):
    count = 0
    for i in classesParents:
        for j in classesParents[i]:
            if j == k:
                count += 1
    print(k,  ':', count)
