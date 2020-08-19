import sys

sys.stdin = open("sample_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())

    sort_row_one = [1,1,0,0]
    sort_row_two = [0,0,1,1]

    sort_row_sum_one = 2*(N//4) + sum(sort_row_one[:N%4])
    sort_row_sum_two = 2*(N//4) + sum(sort_row_two[:N%4])

    result = 0
    two_trigger = True
    for i in range(1,M+1):
        if two_trigger: result += sort_row_sum_one
        else: result += sort_row_sum_two
        if i % 2 == 0: two_trigger = not(two_trigger)

    print("#{}".format(test_case), result)
    # ///////////////////////////////////////////////////////////////////////////////////
