import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    max_part_sum = 0
    max_all_sum = 0
    for _ in range(N):
        a = int(input())
        if max_part_sum + a <= 0: max_part_sum = 0
        if max_part_sum + a > 0: max_part_sum += a
        if max_part_sum > max_all_sum : max_all_sum = max_part_sum
        print(max_part_sum,max_all_sum)

    print("#{}".format(test_case),max_all_sum)
    # ///////////////////////////////////////////////////////////////////////////////////
