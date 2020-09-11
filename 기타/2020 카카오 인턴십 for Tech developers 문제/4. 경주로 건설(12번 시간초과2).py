from collections import deque

def isSafe(y,x,N,board):
    return 0<=y<N and 0<=x<N and board[y][x] != 1

def solution(board):
    N = len(board)

    bways = [[(-1,9999999)] * N for _ in range(N)]

    Q = deque()

    # 왼,아래,오,위
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    fw = {2:0 , 3:1, 0:2, 1:3}

    bways[0][0] = (-1, 0)
    if board[0][1] != 1:
        bways[0][1] = (1<<0,100)
        Q.append((0, 1))
    if board[1][0] != 1:
        bways[1][0] = (1<<3,100)
        Q.append((1, 0))

    while Q:
        start_y, start_x = Q.pop()
        # print(Q)
        for i in range(4):
            new_y = start_y + dy[i]
            new_x = start_x + dx[i]
            if bways[start_y][start_x][0] & 1<<fw[i] != 0:
                dst = bways[start_y][start_x][1] + 100
            else:
                dst = bways[start_y][start_x][1] + 600
            if isSafe(new_y, new_x, N, board) and dst <= bways[new_y][new_x][1]:
                Q.append((new_y,new_x))
                if dst == bways[new_y][new_x][1]:
                    bways[new_y][new_x] = (bways[new_y][new_x][0] | 1 << fw[i], dst)
                else:
                    bways[new_y][new_x] = (1 << fw[i], dst)
            # print(new_y, new_x, i, dst)
            # print(*bways, sep='\n')

    print(*bways, sep='\n')

    return bways[N-1][N-1][1]

board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
solution(board)
print(solution([[0,0,0,0,0],[0,1,1,1,0],[0,0,1,0,0],[1,0,0,0,1],[0,1,1,0,0]]))
print(solution([[0,0,0,0,0],[0,1,1,1,0],[0,0,1,0,0],[1,0,0,0,1],[0,1,1,0,0]]))