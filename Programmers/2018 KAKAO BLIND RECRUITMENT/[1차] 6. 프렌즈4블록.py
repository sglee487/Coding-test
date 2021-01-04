def check_square(board, r, c):
    if board[r][c] != ' ' and board[r][c] == board[r][c + 1] == board[r + 1][c] == board[r + 1][c + 1]:
        return {(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)}
    return set()


def changes(m, n, board):
    changeset = set()
    for r in range(m - 1):
        for c in range(n - 1):
            changeset |= (check_square(board, r, c))
    return list(changeset)


def downboard(m, n, board):
    for r in range(m - 2, -1, -1):
        for c in range(n):
            nr = r
            while nr + 1 < m and board[nr + 1][c] == ' ':
                board[nr + 1][c], board[nr][c] = board[nr][c], board[nr + 1][c]
                nr += 1


def solution(m, n, board):
    board = [list(s) for s in board]
    answer = 0
    while True:
        corrects = changes(m, n, board)
        if not corrects:
            break
        answer += len(corrects)
        for r, c in corrects:
            board[r][c] = ' '
        # print(*board,sep='\n')
        downboard(m, n, board)
    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]),15)