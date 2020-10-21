from bisect import bisect_left, bisect_right
import sys

sys.stdin = open("DP-병사 배치하기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sl = list(map(int, input().split()))
    sl = sl[::-1]

    C = [10000001] * (N + 1)
    C[0] = 0
    LIS = [1] * N

    c_index = 0
    for i, n in enumerate(sl):
        c_index = bisect_left(C, n)
        C[c_index] = n
        LIS[i] = c_index
        # print("i :", i, ", n :", n, ", c_index :", c_index)
        # print("C :", C)
        # print("LIS :", LIS)
    print(N-max(LIS))