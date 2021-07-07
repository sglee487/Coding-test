from collections import deque
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("7576-토마토-5.txt", "r")

input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
empties = 0
for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            Q.append((r,c,0))
        elif box[r][c] == 0:
            empties += 1
if empties == 0:
    print(0)
    exit()

def bfs(Q, empties):
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    count = 0
    while Q:
        r, c, t = Q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if not (0<=nr<N and 0<=nc<M): continue
            if box[nr][nc] != 0: continue
            count += 1
            box[nr][nc] = 1
            Q.append((nr,nc, t+1))
            if count == empties:
                return t+1


    return -1

print(bfs(Q, empties))