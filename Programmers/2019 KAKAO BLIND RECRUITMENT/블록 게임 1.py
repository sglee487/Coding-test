def removegaro(board,r,c):
    for i in range(r,r+2):
        for j in range(c,c+3):
            board[i][j] = 0
    return

def removesero(board,r,c):
    for i in range(r,r+3):
        for j in range(c,c+2):
            board[i][j] = 0
    return

def findgaro(board):
    N = len(board)
    for r in range(N - 1):
        for c in range(N - 2):
            if typegaro1(board,r,c):
                isempty = True
                for sr in range(r+1):
                    if board[sr][c+1] != 0 or board[sr][c+2] != 0:
                        isempty = False
                        break
                if isempty:
                    removegaro(board, r, c)
                    return True
            elif typegaro2(board,r,c):
                isempty = True
                for sr in range(r+1):
                    if board[sr][c] != 0 or board[sr][c+2] != 0:
                        isempty = False
                        break
                if isempty:
                    removegaro(board, r, c)
                    return True
            elif typegaro3(board,r,c):
                isempty = True
                for sr in range(r+1):
                    if board[sr][c] != 0 or board[sr][c+1] != 0:
                        isempty = False
                        break
                if isempty:
                    removegaro(board, r, c)
                    return True
    return False


def findsero(board):
    N = len(board)
    for r in range(N - 2):
        for c in range(N - 1):
            if typesero1(board,r,c):
                isempty = True
                for sr in range(r+2):
                    if board[sr][c] != 0:
                        isempty = False
                        break
                if isempty:
                    removesero(board, r, c)
                    return True
            elif typesero2(board,r,c):
                isempty = True
                for sr in range(r+2):
                    if board[sr][c+1] != 0:
                        isempty = False
                        break
                if isempty:
                    removesero(board,r,c)
                    return True
    return False

def typegaro1(board,r,c):
    if board[r+1][c+1] != 0 and board[r][c] == board[r+1][c] == board[r+1][c+1] == board[r+1][c+2]:
        return True
    return False

def typegaro2(board,r,c):
    if board[r+1][c+1] != 0 and board[r][c+1] == board[r+1][c] == board[r+1][c+1] == board[r+1][c+2]:
        return True
    return False

def typegaro3(board,r,c):
    if board[r+1][c+1] != 0 and board[r][c+2] == board[r+1][c] == board[r+1][c+1] == board[r+1][c+2]:
        return True
    return False

def typesero1(board,r,c):
    if board[r+2][c] != 0 and board[r][c+1] == board[r+1][c+1] == board[r+2][c] == board[r+2][c+1]:
        return True
    return False

def typesero2(board,r,c):
    if board[r+2][c] != 0 and board[r][c] == board[r+1][c] == board[r+2][c] == board[r+2][c+1]:
        return True
    return False


def solution(board):
    answer = 0
    N = len(board)
    # print(*board,sep='\n')
    # print()
    while True:
        # 가로 찾기
        if findgaro(board):
            answer += 1
            continue
        # 세로 찾기
        if findsero(board):
            answer += 1
            continue
        break
    # print(*board, sep='\n')
    # print()
    return answer

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]),2)
print(solution([[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]]),3)
print(solution([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,2,2,0,0,0,0,0],[0,2,1,0,0,0,0,0],[0,2,1,0,0,0,0,0],[0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0]]),1)