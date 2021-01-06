import sys

sys.stdin = open("구현-게임 개발.txt", "r")

N, M = map(int, input().split())
# 위 왼 아래 오
dy = [-1,0,1,0]
dx = [0,-1,0,1]
cr, cc, cd = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
count = 1
print(*board,sep='\n')
while True:
    moved = False
    for i in range(4):
        lr, lc = cr + dy[(cd+i+1)%4], cc + dx[(cd+i+1)%4]
        if 0<=lr<N and 0<=lc<M and board[lr][lc] == 0:
            board[cr][cc] = 1
            cr = lr
            cc = lc
            cd = (cd+i+1)%4
            moved = True
            break
    if not moved:
        board[cr][cc] = 1
        cr, cc = cr + dy[(cd+2)%4], cc + dx[(cd+2)%4]
        if not(0<=cr<N and 0<=cc<M) or board[cr][cc] == 1:
            break
    print(*board, sep='\n')
    count += 1
print(count)