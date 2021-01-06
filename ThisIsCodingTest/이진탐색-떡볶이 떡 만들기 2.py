import sys

sys.stdin = open("이진탐색-떡볶이 떡 만들기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    dducks = list(map(int, input().split()))
    start = 0
    end = max(dducks)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total_dduck = sum([e-mid for e in dducks if e-mid>0])
        if total_dduck >= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result)