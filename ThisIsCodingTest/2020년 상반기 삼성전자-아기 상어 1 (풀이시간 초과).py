from collections import deque
import sys

sys.stdin = open("2020년 상반기 삼성전자-아기 상어.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에

fishlist = [1,2,3,4,5,6]

def calculatemap(board,sharkr,sharkc,sharksize):
    # 위 오 아래 왼
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    dmap = [[10e9] * (N) for _ in range(N)]
    dmap[sharkr][sharkc] = 0
    fishes = []
    Q = deque()
    Q.append((sharkr,sharkc,0))
    while Q:
        r, c, dist = Q.popleft()
        if dist < dmap[r][c]: continue
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if not (0<=nr<N and 0<=nc<N): continue
            if board[nr][nc] > sharksize: continue
            if dist + 1 < dmap[nr][nc]:
                Q.append((nr,nc,dist+1))
                dmap[nr][nc] = dist + 1
                if board[nr][nc] in fishlist and board[nr][nc] < sharksize:
                    fishes.append((dist+1,nr,nc))
    return sorted(fishes), dmap


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # print(*board,sep='\n')
    sharkr, sharkc = 0, 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 9:
                sharkr, sharkc = r, c
    # print()
    sharksize = 2
    sharkstomach = 0
    move = 0
    while True:
        fishes, dmap = calculatemap(board,sharkr,sharkc,sharksize)
        if not fishes: break
        efd, efr, efc = fishes[0][0], fishes[0][1], fishes[0][2]
        board[efr][efc] = 0
        board[sharkr][sharkc] = 0
        move += efd
        sharkr, sharkc = efr,efc
        sharkstomach += 1
        if sharkstomach == sharksize:
            sharksize += 1
            sharkstomach = 0
        # print(*board,sep='\n')
        # print(fishes)
        # print()

    print(move)