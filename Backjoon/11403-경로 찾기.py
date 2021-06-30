from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11403-경로 찾기-2.txt", "r")

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N

def dfs(start, s, visited):
    for i in range(N):
        if matrix[s][i] == 1 and not visited[i]:
            matrix[start][i] = 1
            visited[i] = True
            dfs(start, i, visited)

    return

for start in range(N):
    dfs(start, start, visited[:])

for m in matrix:
    print(*m)