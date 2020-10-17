from collections import deque
import sys
import copy

sys.stdin = open("DFSBFS-감시 피하기.txt", "r")

def can_miss():
    boardt = copy.deepcopy(board)
    Q = deque()
    for r in range(N):
        for c in range(N):
            if boardt[r][c] == 'T':
                Q.append((r, c))
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    while Q:
        r, c = Q.pop()
        boardt[r][c] = 'T'
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            while 0<=nr<N and 0<=nc<N:
                if boardt[nr][nc] == 'S': return False
                if boardt[nr][nc] == 'O': break
                if boardt[nr][nc] == 'T': break
                if boardt[nr][nc] == 'X':
                    nr, nc = nr + dy[i], nc + dx[i]
    return True

def dfs(n):
    global result
    if n < 3:
        for r in range(N):
            for c in range(N):
                if result == 'YES': return
                if board[r][c] == 'X':
                    board[r][c] = 'O'
                    dfs(n + 1)
                    board[r][c] = 'X'
    else:
        if can_miss():
            result = 'YES'
        else:
            result = 'NO'

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N = int(sys.stdin.readline())
    board = [list(input().split()) for _ in range(N)]
    # print(*board, sep='\n')
    result = ''
    dfs(0)
    print(result)