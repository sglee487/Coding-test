from collections import defaultdict


def leftlink(graph, nodedict, lx, rootx, rooty, nowstep, ysteps, nodeinfo):
    now = nodedict[(rootx, rooty)]
    if nowstep + 1 == len(ysteps): return
    for x, y in nodeinfo:
        if ysteps[nowstep + 1] == y:
            if lx <= x <= rootx:
                graph[now].append(nodedict[(x, y)])
                leftlink(graph, nodedict, lx, x, y, nowstep + 1, ysteps, nodeinfo)
                rightlink(graph, nodedict, rootx, x, y, nowstep + 1, ysteps, nodeinfo)


def rightlink(graph, nodedict, rx, rootx, rooty, nowstep, ysteps, nodeinfo):
    now = nodedict[(rootx, rooty)]
    if nowstep + 1 == len(ysteps): return
    for x, y in nodeinfo:
        if ysteps[nowstep + 1] == y:
            if rootx <= x <= rx:
                graph[now].append(nodedict[(x, y)])
                leftlink(graph, nodedict, rootx, x, y, nowstep + 1, ysteps, nodeinfo)
                rightlink(graph, nodedict, rx, x, y, nowstep + 1, ysteps, nodeinfo)

    return


def dfs(now, preorder, graph):
    preorder.append(now)
    for child in graph[now]:
        dfs(child, preorder, graph)
    return preorder


def bdfs(now, lastorder, graph):
    for child in graph[now]:
        bdfs(child, lastorder, graph)
    lastorder.append(now)
    return lastorder


def solution(nodeinfo):
    N = len(nodeinfo)
    ysteps = set()
    rootnum = 0
    rootx, rooty = 0, 0
    nodedict = defaultdict(int)
    maxx = 0
    for i, (x, y) in enumerate(nodeinfo, 1):
        maxx = max(x, maxx)
        nodedict[(x, y)] = i
        ysteps.add(y)
        if y > rooty:
            rootnum = i
            rootx, rooty = x, y
    ysteps = sorted(list(ysteps), reverse=True)
    graph = [[] for _ in range(N + 1)]
    leftlink(graph, nodedict, 0, rootx, rooty, 0, ysteps, nodeinfo)
    rightlink(graph, nodedict, maxx, rootx, rooty, 0, ysteps, nodeinfo)
    preorder = dfs(nodedict[(rootx, rooty)], [], graph)
    lastorder = bdfs(nodedict[(rootx, rooty)], [], graph)
    answer = []
    answer.append(preorder)
    answer.append(lastorder)
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]),[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]])