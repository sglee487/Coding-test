import copy
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("BOARDCOVER2-1.txt", "r")

input = sys.stdin.readline

def rotatedBoard(block):
    r = len(block)
    c = len(block[0])
    newBlock = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            newBlock[j][i] = block[i][c-j-1]
    return newBlock


def emptyNum():
    global R,C, board
    empty = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0: empty += 1
    return empty


def setBoard(r,c,relBlock, delta):
    global R,C, board
    result = True
    for br, bc in relBlock:
        nr, nc = r+br, c+bc
        if not(0<=nr<R and 0<=nc<C):
            result = False
            continue
        board[nr][nc] += delta
        if board[nr][nc] > 1:
            result = False

    return result

def dfs(nownum):
    global R, C, H, W, board, relBlocks, best

    if emptyNum() + nownum <= best:
        return

    i, j = -1, -1
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                i, j = r, c
                break
        if i != -1: break

    if i == -1:
        best = max(best, nownum)
        return

    for relBlock in relBlocks:
        if setBoard(i, j, relBlock, 1):
            dfs(nownum + 1)
        setBoard(i, j, relBlock, -1)
    board[i][j] = 1
    dfs(nownum)
    board[i][j] = 0


def generateRelBlocks(block):
    global R, C, H, W, board, relBlocks, best
    relBlocks = []
    for _ in range(4):
        relBlock = []
        lenR, lenC = len(block), len(block[0])
        originR, originC = -1, -1
        for r in range(lenR):
            for c in range(lenC):
                if block[r][c] == 1:
                    if originR == -1:
                        originR, originC = r, c
                    relBlock.append((r-originR, c-originC))
        relBlocks.append(relBlock)
        block = rotatedBoard(block)
    newRelBlocks = []
    if relBlocks[0] == relBlocks[2]:
        newRelBlocks.append(relBlocks[0])
    else:
        newRelBlocks.append(relBlocks[0])
        newRelBlocks.append(relBlocks[2])
    if relBlocks[1] == relBlocks[3]:
        newRelBlocks.append(relBlocks[1])
    else:
        newRelBlocks.append(relBlocks[1])
        newRelBlocks.append(relBlocks[3])

    return newRelBlocks



def solve():
    global R,C,H,W,board, best
    dfs(0)

    return best


T = int(input())
for _ in range(T):
    R, C, H, W = map(int, input().split())
    board = [list(map(lambda x:1 if x=='#' else 0,input().strip())) for _ in range(R)]
    block = [list(map(lambda x:1 if x=='#' else 0,input().strip())) for _ in range(H)]
    relBlocks = generateRelBlocks(block)

    best = 0
    print(solve())