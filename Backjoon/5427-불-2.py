import sys
sys.setrecursionlimit(10**9)
from collections import deque


sys.stdin = open("5427-불-1.txt", "r")

input = sys.stdin.readline


def simulator():
    global building, fires, guns, w, h
    time = 1
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    while guns:
        for _ in range(len(fires)):
            fire_r, fire_c = fires.popleft()
            for i in range(4):
                nr, nc = fire_r + dy[i], fire_c + dx[i]
                if not (0<=nr<h and 0<=nc<w): continue
                if building[nr][nc] != '.': continue
                building[nr][nc] = '*'
                fires.append((nr,nc))

        for _ in range(len(guns)):
            gun_r, gun_c = guns.popleft()
            for i in range(4):
                nr, nc = gun_r + dy[i], gun_c + dx[i]
                if not (0 <= nr < h and 0 <= nc < w):
                    return time
                if building[nr][nc] != '.': continue
                building[nr][nc] = '@'
                guns.append((nr, nc))
        time += 1
    return 'IMPOSSIBLE'


TEST_CASE = int(input())
for _ in range(TEST_CASE):
    w, h = map(int, input().split())
    building = [[c for c in input().strip()] for _ in range(h)]
    # print(*building, sep='\n')
    fires = deque()
    guns = deque()
    for r in range(h):
        for c in range(w):
            if building[r][c] == '*':
                fires.append((r,c))
            elif building[r][c] == '@':
                guns.append((r,c))

    print(simulator())