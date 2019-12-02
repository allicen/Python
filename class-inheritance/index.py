graph = {}

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.__contains__(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

x = int(input())

while x > 0:
    stringIn = input()
    stringArr = stringIn.split(' : ')
    className = stringArr[0]
    if len(stringArr) == 1:
        if className not in graph:
            graph.update({className: []})
    else:
        classesArr = stringArr[1].split(' ')
        if className in graph:
            classesArr += graph[className]
            graph.update({className: classesArr})
        else:
            graph.update({className: classesArr})
    x -= 1

y = int(input())

while y > 0:
    stringIn = input()
    stringArr = stringIn.split(' ')
    parent = stringArr[0]
    child = stringArr[1]
    if find_path(graph, child, parent) is None:
        print('No')
    else:
        print('Yes')
    y -= 1
