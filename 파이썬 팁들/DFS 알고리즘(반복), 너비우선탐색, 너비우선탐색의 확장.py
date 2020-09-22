# 파이썬 SW문제해결 응용_구현 - 06 그래프의 기본과 탐색

# DFS 알고리즘 - 반복
# G : 그래프, S : 스택, v : 시작 정점
# visited: 정점의 방문 정보 표시, Flase 로 초기화
# G[v]: 그래프 G에서 v의 인접 정점 집합
def DFS_Iterative(S, v):
    S = [v]
    while S:
        v = S.pop()
        if v not in visited:
            visited.append(v)
            visit()
            S.extend(G[v] - set(visited))
    return vistied

# 너비 우선 탐색 알고리즘
# G : 그래프, Q : 큐, v : 시작 정점
# visited: 정점의 방문 정보 표시, Flase 로 초기화
# G[v]: 그래프 G에서 v의 인접 정점 리스트
def BFS(Q, v):
    Q.append(v)
    vistied[v] = True
    visit(v)
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = True
                visit(w)

# 너비 우선 탐색의 확장 알고리즘
# D[]: 최단 거리, P[]: 최단 경로
def BFS(Q, v):
    D[v] = 0
    P[v] = v
    Q.append(v)
    vistied[v] = True
    visit(v)
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = True
                visit(w)
                D[w] = D[v] + 1
                P[w] = v

import sys

sys.stdin = open("input.txt", "r")

def dfs(n,value,used_list):
    global result_product
    if n == N:
        if result_product < value:
            result_product = value
        return

    if value < result_product:
        return

    for i in range(N):
        if i in used_list: continue
        used_list.append(i)
        dfs(n+1,value * (Percents[n][i]/100),used_list)
        used_list.remove(i)

    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    Percents = []
    for _ in range(N):
        Percents.append(list(map(int, input().split())))

    print(Percents)

    result_product = 0.000000

    dfs(0,1,[])

    print(result_product)

    print("#{}".format(test_case),"{:6f}".format(result_product*100))
    # ///////////////////////////////////////////////////////////////////////////////////
