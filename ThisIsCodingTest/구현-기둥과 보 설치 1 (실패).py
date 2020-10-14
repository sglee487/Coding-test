# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    board = [[-1] * (n+1) for _ in range(n+1)]
    for x, y, a, b in build_frame:
        if a == 0:
            if b == 0:
                if y != 0 and board[y-1][x-1] != 1 and board[y-1][x] != 0: continue
                board[y][x] = -1
            if b == 1:
                if y == 0 or board[y][x-1] == 1 or board[y][x] == 1 or board[y-1][x] == 0:
                    board[y][x] = 0
        if a == 1:
            if b == 0:
                if board[y-1][x] != 0 and board[y-1][x+1] != 0: continue
                if x < n-1 and board[y-1][x+2] != 0: continue
                board[y][x] = -1
            if b == 1:
                if (board[y-1][x] == 0 or board[y-1][x+1] == 0) or (board[y][x-1] == 1 and board[y][x+1] == 1):
                    board[y][x] = 1
    print(*board,sep='\n')
    answer = []
    for y in range(n+1):
        for x in range(n+1):
            if board[y][x] >= 0:
                answer.append([x,y,board[y][x]])
    answer.sort()
    print(answer)
    return answer

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]),[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]])