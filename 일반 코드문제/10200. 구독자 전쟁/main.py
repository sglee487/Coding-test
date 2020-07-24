import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, A, B = map(int, input().split())

    intersection = min(A,B)
    bigger_value = max(A,B)
    complementary = intersection - (N - bigger_value) if intersection - (N - bigger_value) >= 0 else 0

    print("#{}".format(test_case),intersection,complementary)

    # ///////////////////////////////////////////////////////////////////////////////////
