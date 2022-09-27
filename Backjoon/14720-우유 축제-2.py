import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("14720-우유 축제-2.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))

now = 0
for milk in nl:
    if now%3 == milk:
        now += 1
print(now)