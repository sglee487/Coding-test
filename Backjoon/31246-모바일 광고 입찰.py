import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("31246-모바일 광고 입찰-2.txt", "r")

# input = sys.stdin.readline

N, K = map(int, input().split())

remains = []

for _ in range(N):
    a, b = map(int, input().split())
    remains.append(a-b)

remains.sort(reverse=True)

if remains[K-1] < 0:
    print(abs(remains[K-1]))
else:
    print(0)