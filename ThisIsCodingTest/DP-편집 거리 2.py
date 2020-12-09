import sys

sys.stdin = open("DP-편집 거리.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    A = list(input())
    B = list(input())
    A = [''] + A
    B = [''] + B
    print(A)
    lena = len(A)
    lenb = len(B)
    print(A,B)
    board = [[9999] * (lena) for _ in range(lenb)]
    for r in range(lena):
        board[0][r] = r
    for c in range(lenb):
        board[c][0] = c
    for r in range(1,lenb):
        for c in range(1,lena):
            if A[c] == B[r]: board[r][c] = board[r-1][c-1]
            else: board[r][c] = min(board[r-1][c],board[r][c-1],board[r-1][c-1]) + 1
    print(*board, sep='\n')
    print(board[lenb-1][lena-1])