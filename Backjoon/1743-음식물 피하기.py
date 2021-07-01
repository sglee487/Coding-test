import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("1743-음식물 피하기-1.txt", "r")

input = sys.stdin.readline

N, M, K = map(int, input().split())

hall = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    hall[r-1][c-1] = 1

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(hall, visited, r, c):
    size = 1
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0<=nr<N and 0<=nc<M): continue
        if hall[nr][nc] != 1 or visited[nr][nc]: continue
        visited[nr][nc] = True
        size += dfs(hall, visited, nr, nc)
    return size

answer = 0
for r in range(N):
    for c in range(M):
        if hall[r][c] == 1 and not visited[r][c]:
            visited[r][c] = True
            answer = max(answer, dfs(hall, visited, r, c))


print(answer)