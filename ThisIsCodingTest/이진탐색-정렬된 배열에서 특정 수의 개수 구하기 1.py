from bisect import bisect_left, bisect_right
import sys

sys.stdin = open("이진탐색-정렬된 배열에서 특정 수의 개수 구하기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, x = map(int, input().split())
    a = list(map(int, input().split()))
    result = bisect_right(a,x) - bisect_left(a,x)
    print(result) if result > 0 else print(-1)