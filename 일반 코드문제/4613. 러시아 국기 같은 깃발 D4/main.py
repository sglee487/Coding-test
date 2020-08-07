import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    print(*board,sep='\n')

    # WB = [1 if c == 'W' else 0 for s in board for c in s] # work
    # WB = [1 if c == 'W' else 0 for c in s for s in board] # not work
    WB = [[1 if c == 'W' else 0 for c in s] for s in board]
    BB = [[1 if c == 'B' else 0 for c in s] for s in board]
    RB = [[1 if c == 'R' else 0 for c in s] for s in board]

    wsl, bsl, rsl = 0, 0, 0
    max_avg = 0
    print(sum(WB[0]))
    # white
    # for i in range(wsl,N-2):
    #     avg =


    print("#{}".format(test_case))
    # ///////////////////////////////////////////////////////////////////////////////////
