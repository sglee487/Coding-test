import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("14503-로봇 청소기-2.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

count = 0

def clean(r,c,d,t):
    global board, N, M, count
    if t == 4:
        back_r, back_c = r + dy[d-2], c + dx[d-2]
        if board[back_r][back_c] == 2:
            clean(back_r, back_c, d, 0)
        return
    if board[r][c] == 0:
        count += 1
    board[r][c] = 2
    left_d = (d-1) % 4
    left_r, left_c = r + dy[left_d], c + dx[left_d]
    if 0<=left_r<N and 0<=left_c<M and board[left_r][left_c] == 0:
        clean(left_r,left_c, left_d,0)
    else:
        clean(r,c,left_d, t+1)

clean(r,c,d, 0)

print(count)