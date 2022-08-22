from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11403-경로 찾기-2.txt", "r")

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

answer = [[0] * N for _ in range(N)]


def find_ways(start):
    global N, graph, answer
    Q = deque()
    visited = [False] * N
    Q.append(start)
    while Q:
        now = Q.pop()
        for nxt, pos in enumerate(graph[now]):
            if pos and not visited[nxt]:
                visited[nxt] = True
                answer[start][nxt] = 1
                Q.append(nxt)


for i in range(N):
    find_ways(i)

for ans in answer:
    print(*ans)
