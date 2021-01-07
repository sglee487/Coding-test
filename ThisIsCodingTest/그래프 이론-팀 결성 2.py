import sys

sys.stdin = open("그래프 이론-팀 결성.txt", "r")

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
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
    parent = list(range(N+1))
    for _ in range(M):
        com, a, b = map(int, input().split())
        if com == 0:
            union_parent(parent,a,b)
        elif com == 1:
            if find_parent(parent,a) == find_parent(parent,b):
                print('YES')
            else:
                print("NO")