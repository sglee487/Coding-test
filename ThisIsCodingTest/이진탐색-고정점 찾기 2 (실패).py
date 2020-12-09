from bisect import bisect_left, bisect_right
import sys

sys.stdin = open("이진탐색-고정점 찾기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    bl,br = 0, N-1
    print(bisect_left(numbers,bl))
    print(bisect_right(numbers,br))
    while br-bl != 1 and br>bl:
        if bisect_left(numbers,bl) > bl:
            bl = (br+bl)//2
        if bisect_right(numbers,br) < br:
            br = (br-bl)//2
        print(bl,br)