import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    D, H, M = map(int, input().split())

    d, h, m = D-11, H-11, M-11

    total_m = d*1440 + h*60 + m

    print("#{}".format(test_case),total_m if total_m >= 0 else -1)
    # ///////////////////////////////////////////////////////////////////////////////////
