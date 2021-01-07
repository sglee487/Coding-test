# https://www.acmicpc.net/problem/1647
import sys
import heapq

sys.stdin = open("그래프 이론-도시 분할 계획.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    HQ = []
    streettotal = 0
    for _ in range(M):
        A, B, C = map(int, input().split())
        heapq.heappush(HQ,(C,A,B))
        streettotal += C
    parent = list(range(N+1))
    connectedtotal = 0
    lastst = 0
    while HQ:
        st, a, b = heapq.heappop(HQ)
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            connectedtotal += st
            lastst = st
    print(connectedtotal - lastst)