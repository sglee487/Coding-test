import sys

sys.stdin = open("이진탐색-고정점 찾기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nl = list(map(int, input().split()))
    l = 0
    r = N-1
    result = -1
    while l <= r:
        mid = (l+r) // 2
        if nl[mid] < mid:
            l = mid+1
        elif nl[mid] > mid:
            r = mid-1
        else:
            result = mid
            break
    print(result)