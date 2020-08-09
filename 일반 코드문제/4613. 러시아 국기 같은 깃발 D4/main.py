import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    # print(*board,sep='\n')

    # WB = [1 if c == 'W' else 0 for s in board for c in s] # work
    # WB = [1 if c == 'W' else 0 for c in s for s in board] # not work
    WNB = [[0 if c == 'W' else 1 for c in s] for s in board]
    BNB = [[0 if c == 'B' else 1 for c in s] for s in board]
    RNB = [[0 if c == 'R' else 1 for c in s] for s in board]

    result = 2500

    for blue_start in range(1, N - 1):
        for blue_size in range(1, N - blue_start):
            # print("blue_start :", blue_start)
            # print("blue_size :", blue_size)

            all_sum = 0

            for i in range(0,blue_start):
                # print("i :", i)
                all_sum += sum(WNB[i])

            for j in range(blue_start, blue_start + blue_size):
                # print("j :", j)
                all_sum += sum(BNB[j])

            for k in range(blue_start + blue_size, N):
                # print("k :", k)
                all_sum += sum(RNB[k])

            if result > all_sum:
                result = all_sum

    print("#{}".format(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////
