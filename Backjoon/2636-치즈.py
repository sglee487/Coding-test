from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2636-치즈-1.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

Q = deque()
for r in range(N):
    Q.append((r,0))
    Q.append((r,M-1))
    visited[r][0] = True
    visited[r][M-1] = True
for c in range(1, M-1):
    Q.append((0,c))
    Q.append((N-1,c))
    visited[0][c] = True
    visited[N-1][c] = True

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

time = 0
last_cheese = 0
next_Q = deque()
while True:
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            new_r, new_c = r + dy[i], c + dx[i]
            if 0<=new_r<N and 0<=new_c<M and not visited[new_r][new_c]:
                visited[new_r][new_c] = True
                if board[new_r][new_c] == 0:
                    Q.append((new_r,new_c))
                elif board[new_r][new_c] == 1:
                    next_Q.append((new_r, new_c))
    if len(next_Q) == 0:
        break
    last_cheese = len(next_Q)
    while next_Q:
        r, c = next_Q.popleft()
        Q.append((r,c))
        board[r][c] = 0
    time += 1

print(time)
print(last_cheese)