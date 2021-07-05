from collections import deque
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("6593-상범 빌딩-1.txt", "r")

input = sys.stdin.readline

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0): break

    building = []
    for _ in range(L):
        building.append([list(input().strip()) for _ in range(R)])
        input()
    distance = [[[0] * C for _ in range(R)] for _ in range(L)]

    S = (-1, -1, -1)
    E = (-1, -1, -1)
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == 'S':
                    S = (l,r,c)
                if building[l][r][c] == 'E':
                    E = (l,r,c)
    # 위 오 아래 왼 하늘 땅
    dz = [0,0,0,0,1,-1]
    dy = [-1,0,1,0,0,0]
    dx = [0,1,0,-1,0,0]
    Q = deque()
    Q.append(((S),1))
    distance[S[0]][S[1]][S[2]] = 1
    answer = -1
    while Q:
        (f,r,c),d = Q.popleft()
        if E == (f, r, c):
            answer = d
            break
        for i in range(6):
            nf, nr, nc = f + dz[i], r + dy[i], c + dx[i]
            if not (0<=nf<L and 0<=nr<R and 0<=nc<C): continue
            if building[nf][nr][nc] == '#' or distance[nf][nr][nc]: continue
            distance[nf][nr][nc] = d + 1
            Q.append(((nf, nr, nc), d+1))
    if answer != -1:
        print(f"Escaped in {answer-1} minute(s).")
    else:
        print("Trapped!")