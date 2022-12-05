import sys

sys.stdin = open('구현-게임 개발.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 위 오 아래 왼
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited = [[False] * M for _ in range(N)]
visited[r][c] = True

turn_time = 0
while True:
    d = (d - 1) % 4
    nr, nc = r + dy[d], c + dx[d]
    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0 and not visited[nr][nc]:
        visited[nr][nc] = True
        turn_time = 0
        r, c = nr, nc
        continue
    turn_time += 1
    if turn_time == 4:
        nr, nc = r + dy[(d - 2) % 4], c + dx[(d - 2) % 4]
        if board[nr][nc] == 1:
            break
        r, c = nr, nc
        turn_time = 0


answer = sum(map(sum, visited))
print(answer)