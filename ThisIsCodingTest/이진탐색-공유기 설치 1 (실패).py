from bisect import bisect_left, bisect_right
import sys

sys.stdin = open("이진탐색-공유기 설치.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, C = map(int, input().split())
    clist = [0] * C
    for _ in range(N):
        n = int(input())
        index = bisect_left(clist,n)
        leftd = n - clist[index-1] if index-1>=0 else 0
        rightd = clist[index+1] - n if index+1<C else 0
        leftod = clist[index] - clist[index-1] if index-1>=0 else 0
        rightod = clist[index+1] - clist[index] if index+1<C else 0
        if leftd > leftod and rightd > rightod:
            C[index] = n
    print(clist)