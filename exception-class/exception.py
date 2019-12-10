graph = {}
inputExc = set()


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


n = int(input())
while n > 0:
    strIn = input()
    strArr = strIn.split(' : ')
    exceptionName = strArr[0]
    if len(strArr) == 1:
        if exceptionName not in graph:
            graph.update({exceptionName: set()})
    else:
        exceptionArr = strArr[1].split(' ')
        if exceptionName in graph:
            exceptionArr += graph[exceptionName]
            graph.update({exceptionName: set(exceptionArr)})
        else:
            graph.update({exceptionName: set(exceptionArr)})
    n -= 1


n = int(input())
while n > 0:
    strIn = input()
    for ex in inputExc:
        if find_path(graph, strIn, ex) is not None:
            print(strIn)
            break
    inputExc.add(strIn)
    n -= 1
