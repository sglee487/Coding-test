import sys

sys.stdin = open("input.txt", "r")

def check_around(r,c):
    # 아래, 우측아래, 우측, 우측위, 위, 좌측위, 좌측, 좌측아래
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    mine_count = 0
    for d in range(8):
        y = r + dy[d]
        x = c + dx[d]
        if 0 <= x < N and 0 <= y < N:
            if board[y][x] == '*': mine_count += 1

    return mine_count

def click_zero(r,c):
    # 아래, 우측아래, 우측, 우측위, 위, 좌측위, 좌측, 좌측아래
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    board[r][c] = 'C'
    for d in range(8):
        y = r + dy[d]
        x = c + dx[d]
        if 0 <= x < N and 0 <= y < N:
            if board[y][x] == 0:
                click_zero(y,x)
            board[y][x] = 'C'


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(input()))


    for r in range(N):
        for c in range(N):
            if board[r][c] == '.':
                board[r][c] = check_around(r,c)

    zero_click_count = 0

    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                click_zero(r,c)
                zero_click_count += 1

    count_numbers = 0

    for r in range(N):
        for c in range(N):
            if board[r][c] != 'C' and board[r][c] != '*':
                count_numbers += 1

    result = count_numbers + zero_click_count

    print("#{}".format(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////
