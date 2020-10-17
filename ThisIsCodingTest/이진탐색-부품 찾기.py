from bisect import bisect_left, bisect_right
import sys

sys.stdin = open("이진탐색-부품 찾기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nlist = list(map(int, input().split()))
    M = int(input())
    mlist = list(map(int, input().split()))
    result = ['no'] * M
    mlist.sort()
    for n in nlist:
        index = bisect_left(mlist,n)
        if mlist[index] == n:
            result[index] = 'yes'
    print(result)