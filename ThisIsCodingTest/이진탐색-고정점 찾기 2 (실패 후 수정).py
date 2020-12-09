import sys

sys.stdin = open("이진탐색-고정점 찾기.txt", "r")

# https://github.com/ndb796/Python-Competitive-Programming-Team-Notes/blob/master/Searching/binary_search.py
def binary_search(array,start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            return binary_search(array,start,mid-1)
        else:
            return binary_search(array,mid+1,end)
    return None

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    index = binary_search(numbers,0,N-1)
    if index == None:
        print(-1)
    else:
        print(index)