from bisect import bisect_left, bisect_right
import sys

sys.stdin = open("이진탐색-떡볶이 떡 만들기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nlist = list(map(int, input().split()))
    start = 0
    end = max(nlist)
    H = int()
    result = 0
    while start <= end:
        H = (start + end) // 2
        all_sum = 0
        for n in nlist:
            if n - H > 0:
                all_sum += n - H
        if all_sum < M:
            end = H - 1
        elif all_sum == M:
            result = H
            start = H + 1
        else:
            start = H + 1
    print(result)