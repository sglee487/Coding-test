from bisect import bisect_left, bisect_right
import sys

sys.stdin = open("이진탐색-고정점 찾기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    number = list(map(int, input().split()))
    result = -1
    for i in range(N):
        indl = bisect_left(number,number[i])
        ind = bisect_right(number,number[i])
        if number[i] < bisect_right(number,number[i]):
            continue
        elif number[i] == bisect_right(number,number[i]):
            result = i
            break
        else:
            result = -1
            break
    print(result)