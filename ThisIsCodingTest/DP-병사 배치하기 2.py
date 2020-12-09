from bisect import bisect_left
import sys

sys.stdin = open("DP-병사 배치하기.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sl = list(map(int, input().split()))
    sl = sl[::-1]

    C = [10000001] * (N + 1)
    C[0] = 0
    LIS = [1] * N
    for i, e in enumerate(sl):
        c_index = bisect_left(C,e)
        C[c_index] = e
        LIS[i] = c_index
    print(N-max(LIS))