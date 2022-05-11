import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("BLOCKGAME-1.txt", "r")

input = sys.stdin.readline


def cellToInt(r,c):
    return 1 << ((r*5) + c)


def makeMoves():
    global moves
    for r in range(4):
        for c in range(4):
            cells = []
            for dr in range(2):
                for dc in range(2):
                    cells.append(cellToInt(r+dr,c+dc))
            for i in range(4):
                moves.append(cells[0]+cells[1]+cells[2]+cells[3]-cells[i])
    for i in range(5):
        for j in range(4):
            moves.append(cellToInt(i,j) + cellToInt(i,j+1))
            moves.append(cellToInt(j,i) + cellToInt(j+1,i))


def convertBoardToInt(board):
    boardInt = 0
    for r in range(5):
        for c in range(5):
            if board[r][c] == '#': boardInt += cellToInt(r,c)
    return boardInt


def play(boardInt):
    global cache
    if cache[boardInt] != -1:
        return cache[boardInt]

    for move in moves:
        if (move & boardInt) == 0:
            if not play(boardInt | move):
                cache[boardInt] = True
                return True
    cache[boardInt] = False
    return False


C = int(input())
for _ in range(C):
    board = [list(input().strip()) for _ in range(5)]
    # print(*board, sep='\n')
    cache = [-1] * (2**25)
    moves = []
    makeMoves()
    boardInt = convertBoardToInt(board)
    if play(boardInt):
        print('WINNING')
    else:
        print('LOSING')