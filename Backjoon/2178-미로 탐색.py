from collections import deque
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("2178-미로 탐색-1.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]
mirod = [[0] * M for _ in range(N)]
Q = deque()
answer = int()
Q.append((0,0,1))
mirod[0][0] = 1
while Q:
    r, c, d = Q.popleft()
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0<=nr<N and 0<=nc<M): continue
        if miro[nr][nc] != 1 or mirod[nr][nc]: continue
        mirod[nr][nc] = d+1
        Q.append((nr,nc,d+1))
        if (nr, nc) == (N-1,M-1):
            answer = d+1
            break

print(answer)