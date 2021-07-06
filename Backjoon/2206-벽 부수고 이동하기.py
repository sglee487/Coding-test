from collections import deque
import sys

sys.setrecursionlimit(10**9)

sys.stdin = open("2206-벽 부수고 이동하기-5.txt", "r")

INF = 99999999

input = sys.stdin.readline

# 위 오 아래 왼
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def onload(sr, sc, maps, distances):
    global N, M
    Q = deque()
    Q.append((sr, sc, 1))
    while Q:
        r, c, b = Q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if not (0 <= nr < N and 0 <= nc < M): continue
            if distances[nr][nc][b] != INF: continue
            if maps[nr][nc] == 0:
                distances[nr][nc][b] = distances[r][c][b] + 1
                Q.append((nr,nc,b))
            elif maps[nr][nc] == 1 and b == 1:
                distances[nr][nc][b-1] = distances[r][c][b] + 1
                Q.append((nr, nc, b - 1))
            if (nr, nc) == (N - 1, M - 1):
                return min(distances[nr][nc])
    return INF
def bfs(maps, distances):
    global N, M
    answer = onload(0,0, maps, distances)
    return answer

N, M = map(int, input().split())
if (N,M) == (1,1):
    print(1)
    exit()
maps = [list(map(int, input().strip())) for _ in range(N)]
distances = [[[INF,INF] for _ in range(M)] for _ in range(N)]
distances[0][0] = [1,1]
answer = bfs(maps, distances)
print(answer if answer != INF else -1)