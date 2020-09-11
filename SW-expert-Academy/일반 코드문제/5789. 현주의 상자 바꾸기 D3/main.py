import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, Q = map(int, input().split())
    nl = [0] * N
    for i in range(Q):
        l, r = map(int, input().split())
        nl[l-1:r+1-1] = [i+1] * (r-l+1)

    print("#{}".format(test_case),*nl)
    # ///////////////////////////////////////////////////////////////////////////////////
