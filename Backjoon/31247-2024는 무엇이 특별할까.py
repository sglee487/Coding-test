import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("31247-2024는 무엇이 특별할까-1.txt", "r")

# input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    if K >= 60:
        print(0)
        continue

    a = N >> K
    b = N >> (K+1)
    print(abs(a - b))
