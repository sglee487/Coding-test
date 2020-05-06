import sys

sys.stdin = open("sample_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    AN, BN = map(int, input().split())
    A = [input() for _ in range(AN)]
    B = [input() for _ in range(BN)]

    result = 0
    for a in A:
        for b in B:
            if a == b: result += 1

    print("#{}".format(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
