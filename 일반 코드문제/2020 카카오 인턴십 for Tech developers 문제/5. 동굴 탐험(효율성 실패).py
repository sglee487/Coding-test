# https://medium.com/@haeseok/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8F%99%EA%B5%B4-%ED%83%90%ED%97%98-a669d62f304d
from collections import deque

def dfs_Q():

    check2 = [False] * N
    visited = [False] * N
    Q = deque()
    Q.append((0,visited))
    while Q:
        node, visited = Q.pop()
        visited[node] = True
        check2[node] = True
        for i in dir_graph[node]:
            if visited[i]: return True
            if not check2[i]:
                Q.append((i, visited))
        visited[node] = False

    return False

def solution(n, path, order):
    global dir_graph, N

    N = n
    graph = [[] for _ in range(N)]

    for A, B in path:
        graph[A].append(B)
        graph[B].append(A)

    dir_graph = [[] for _ in range(N)]
    check = [False] * N

    Q = deque([0])
    check[0] = True
    while Q:
        node = Q.popleft()
        for i in graph[node]:
            if check[i]: continue
            check[i] = True
            dir_graph[node].append(i)
            Q.append(i)

    for A, B in order:
        dir_graph[A].append(B)
    # print(dir_graph)

    is_cycle = dfs_Q()
    return not(is_cycle)

print(solution(3,[[0,1],[1,2]],[[1,2]]))
print(solution(3,[[0,1],[1,2]],[[2,1]]))
print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[8,5],[6,7],[4,1]]))
print(solution(9,[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],[[4,1],[5,2]]))
print(solution(9,[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],[[4,1],[8,7],[6,5]]))