import sys

sys.stdin = open("정렬-안테나.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    houses = list(map(int,sys.stdin.readline().split()))
    houses.sort()
    print(houses[(N//2)-1])