import heapq
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("1197-최소 스패닝 트리-1.txt", "r")

input = sys.stdin.readline

V, E = map(int, input().split())
distances = []
tree_set = set()
for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(distances, (C, A, B))

parents = list(range(V + 1))


def FIND_SET(x):
    if parents[x] != x:
        parents[x] = FIND_SET(parents[x])
    return parents[x]


def UNION(x, y):
    parents[FIND_SET(y)] = FIND_SET(x)


answer = 0
while distances and len(tree_set) < V:
    distance, a, b = heapq.heappop(distances)
    if FIND_SET(a) != FIND_SET(b):
        answer += distance
        UNION(a, b)
print(answer)
