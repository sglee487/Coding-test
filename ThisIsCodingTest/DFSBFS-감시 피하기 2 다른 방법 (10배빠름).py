import sys
# https://www.acmicpc.net/problem/18428

sys.stdin = open("DFSBFS-감시 피하기.txt", "r")

def can_hide(board,teachers):
    global N
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    for tr,tc in teachers:
        for i in range(4):
            nr, nc = tr + dy[i], tc + dx[i]
            while 0<=nr<N and 0<=nc<N:
                if board[nr][nc] == 'X':
                    nr, nc = nr + dy[i], nc + dx[i]
                elif board[nr][nc] == 'S':
                    return False
                elif board[nr][nc] == 'T':
                    break
                elif board[nr][nc] == 'O':
                    break
    return True

def dfs(current,count):
    global Teachers, N, Board
    if count == 3:
        return can_hide(Board, Teachers)
    for i in range(current,N*N):
        r, c = i//N, i%N
        if Board[r][c] == 'X':
            Board[r][c] = 'O'
            if dfs(i,count+1):
                return True
            Board[r][c] = 'X'
    return False

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N = int(input())
    Board = [list(sys.stdin.readline().split()) for _ in range(N)]
    # print(*Board,sep='\n')
    # print()
    Students = []
    Teachers = []
    Voids = []
    for r in range(N):
        for c in range(N):
            if Board[r][c] == 'S': Students.append((r,c))
            elif Board[r][c] == 'T': Teachers.append((r,c))
            elif Board[r][c] == 'X': Voids.append((r,c))
    result = dfs(0,0)
    if result: print("YES")
    else: print("NO")