from collections import deque
import sys

sys.setrecursionlimit(10**9)

sys.stdin = open("5427-불-1.txt", "r")

input = sys.stdin.readline

def bfs(building, distances, fires):
    times = 1
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    Q = deque()
    Q.append((gun[0],gun[1], times))
    distances[gun[0]][gun[1]] = 1

    while Q:
        while fires and fires[0][2] == times:
            r, c, t = fires.popleft()
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if not (0<=nr<R and 0<=nc<C): continue
                if not building[nr][nc] in ('@','.'): continue
                building[nr][nc] = '*'
                fires.append((nr,nc, t+1))

        while Q and Q[0][2] == times:
            r, c, t = Q.popleft()
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if not (0<=nr<R and 0<=nc<C): continue
                if not building[nr][nc] == '.': continue
                building[nr][nc] = '@'
                distances[nr][nc] = distances[r][c] + 1
                Q.append((nr,nc, t+1))
                if (nr == 0 or nc == 0 or nr == R-1 or nc == C-1):
                    return t+1

        times += 1
    return 'IMPOSSIBLE'

T = int(input())
for test_case in range(T):
    C, R = map(int, input().split())
    building = [list(input().strip()) for _ in range(R)]

    gun = (-1,-1)
    fires = deque()
    for r in range(R):
        for c in range(C):
            if building[r][c] == '@':
                gun = (r,c)
            if building[r][c] == '*':
                fires.append((r,c,1))
    if (gun[0] == 0 or gun[1] == 0 or gun[0] == R - 1 or gun[1] == C - 1):
        print(1)
        continue
    distances = [[-1] * C for _ in range(R)]
    answer = bfs(building, distances, fires)
    print(answer)
