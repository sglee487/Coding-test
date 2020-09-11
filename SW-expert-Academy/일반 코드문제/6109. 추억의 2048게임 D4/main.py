import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, S = input().split()
    N = int(N)

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    # print(*board, sep='\n')

    # left, down, right, up
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    DIR_DIC = {"left": 0, "down": 1, "right": 2, "up": 3}

    calculated = []

    iter_range = range(N) if S in 'upleft' else range(N-1,-1,-1)

    for r in iter_range:
        for c in iter_range:
            if not(board[r][c]): continue
            old_y, old_x = r, c
            new_y, new_x = old_y + dy[DIR_DIC[S]], old_x + dx[DIR_DIC[S]]
            while 0 <= new_y < N and 0 <= new_x < N:
                if board[new_y][new_x] == 0:
                    board[new_y][new_x], board[old_y][old_x]= board[old_y][old_x], board[new_y][new_x]
                    old_y, old_x = new_y, new_x
                    new_y, new_x = old_y + dy[DIR_DIC[S]], old_x + dx[DIR_DIC[S]]
                elif board[new_y][new_x] == board[old_y][old_x] and (new_y,new_x) not in calculated:
                    board[new_y][new_x] *= 2
                    board[old_y][old_x] = 0
                    calculated.append((new_y,new_x))
                    break
                else: break
                # print(r, c, old_y, old_x)
                # print(*board, sep='\n')
                # print("=")

    # print(*board, sep='\n')

    print("#{}".format(test_case))
    for i in board:
        print(*i)
    # ///////////////////////////////////////////////////////////////////////////////////
