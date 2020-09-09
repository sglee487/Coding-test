from collections import deque

def isSafe(y,x,N,board):
    return 0<=y<N and 0<=x<N and board[y][x] != 1

def solution(board):
    N = len(board)

    Q = deque()

    # 왼,아래,오,위
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    fd = {2:0 , 3:1, 0:2, 1:3}
    dd = {0:"left", 1:"down", 2:"right", 3:"up"}

    ds = [[[9999999,9999999,9999999,9999999] for _ in range(N)] for _ in range(N)]
    cars = []

    ds[0][0][0],ds[0][0][1],ds[0][0][2],ds[0][0][3] = 0,0,0,0
    if board[0][1] != 1:
        ds[0][1][2] = 100
        Q.append((0, 1, 2))
    if board[1][0] != 1:
        ds[1][0][1] = 100
        Q.append((1, 0, 1))

    while Q:
        # print(Q)
        start_y, start_x, dh = Q.popleft()
        for i in range(4):
            if fd[dh] == i: continue # no go back
            new_y = start_y + dy[i]
            new_x = start_x + dx[i]
            if dh == i: dst = ds[start_y][start_x][dh] + 100
            else: dst = ds[start_y][start_x][dh] + 600
            if isSafe(new_y, new_x, N, board) and dst <= ds[new_y][new_x][i]:
                Q.append((new_y,new_x, i))
                ds[new_y][new_x][i] = dst
            # print(start_y, start_x, new_y, new_x, dd[i], dst)
            # print(*ds, sep='\n')

    print(*ds, sep='\n')

    return min(ds[N-1][N-1])

# print(solution(	[[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
# print(solution([[0, 0, 0], [1, 0, 0], [0, 0, 0]]))
print(solution([[0,0,0,0,0],[0,1,1,1,0],[0,0,1,0,0],[1,0,0,0,1],[0,1,1,0,0]]))