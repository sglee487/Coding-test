from collections import deque

def isSafe(y,x,N,board):
    return 0<=y<N and 0<=x<N and board[y][x] != 1

def solution(board):
    N = len(board)

    Q = deque()

    # 왼,아래,오,위
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    fw = {2:0 , 3:1, 0:2, 1:3}

    save_pdd = {(0,0):[1<<0 | 1<<3,0]}
    if board[0][1] != 1:
        save_pdd[(0, 1)] = [1 << 0, 100]
        Q.append((0, 1))
    if board[1][0] != 1:
        save_pdd[(1, 0)] = [1 << 3, 100]
        Q.append((1, 0))

    while Q:
        # print(Q)
        start_y, start_x = Q.pop()
        for i in range(4):
            new_y = start_y + dy[i]
            new_x = start_x + dx[i]
            if save_pdd[(start_y, start_x)][0] & 1<<fw[i] != 0:
                dst = save_pdd[(start_y, start_x)][1] + 100
            else:
                dst = save_pdd[(start_y, start_x)][1] + 600
            if isSafe(new_y,new_x,N,board):
                if (new_y,new_x) not in save_pdd:
                    save_pdd[(new_y, new_x)] = [1 << fw[i], dst]
                    Q.append((new_y, new_x))
                    continue
                if save_pdd[(new_y,new_x)][1] < dst: continue
                if dst == save_pdd[(new_y, new_x)][1]:
                    save_pdd[(new_y, new_x)][0] |= 1 << fw[i]
                else:
                    save_pdd[(new_y, new_x)] = [1 << fw[i], dst]
                    Q.append((new_y, new_x))
            # print(new_y, new_x, i, dst)
            # print(save_pdd, sep='\n')

    # print(*bways, sep='\n')

    return save_pdd[(N-1,N-1)][1]

board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
print(solution(board))
print(solution([[0,0,0,0,0],[0,1,1,1,0],[0,0,1,0,0],[1,0,0,0,1],[0,1,1,0,0]]))