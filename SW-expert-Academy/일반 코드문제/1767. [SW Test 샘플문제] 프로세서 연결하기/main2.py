import sys

def dfs(coreindex,ccore,tw):
    global gcore, gways
    if coreindex == CN:
        if ccore > gcore:
            gcore = ccore
            gways = 999999
        if gcore == ccore:
            gways = min(gways,tw)
        # print(*board, sep='\n')
        # print(ccore,tw)
        return
    r, c = cores[coreindex]
    all_cantconnect = True
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        way = 0
        while 0<=nr<N and 0<=nc<N and board[nr][nc] == 0:
            board[nr][nc] = N+coreindex
            nr, nc = nr + dy[i], nc + dx[i]
            way += 1
        if nr == -1 or nr == N or nc == -1 or nc == N:
            all_cantconnect = False
            dfs(coreindex+1, ccore + 1,tw + way)
        nr, nc = r + dy[i], c + dx[i]
        while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == N+coreindex:
            board[nr][nc] = 0
            nr, nc = nr + dy[i], nc + dx[i]
    if all_cantconnect: dfs(coreindex + 1, ccore, tw)

    return

sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
T = int(input())
for test_case in range(1, T + 1):
    global cores, board, N, CN, dy, dx, gcore, gways
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # print(*board,sep='\n')

    cores = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1: cores.append((r,c))
    # print(cores)

    CN = len(cores)

    gcore = 0
    gways = 99999999
    # 위 오른쪽 아래 왼쪽
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    dfs(0,0,0)
    # print(gcore,gways)
    print("#{}".format(test_case),gways)