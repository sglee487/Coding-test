import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("14500-테트로미노-3.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 위 오 아래 왼
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0

visited = [[False] * M for _ in range(N)]
def dfs(step, r, c, total):
    global answer
    if step == 3:
        answer = max(answer, total)
        return

    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0<=nr<N and 0<=nc<M): continue
        if visited[nr][nc]: continue
        visited[nr][nc] = True
        dfs(step+1, nr, nc, total + board[nr][nc])
        visited[nr][nc] = False
        if step == 1:
            visited[nr][nc] = True
            dfs(step + 1, r, c, total + board[nr][nc])
            visited[nr][nc] = False

for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(0,r,c,board[r][c])
        visited[r][c] = False

print(answer)