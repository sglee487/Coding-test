import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("11729-하노이 탑 이동 순서-1.txt", "r")

input = sys.stdin.readline

N = int(input())

def dfs(n):
    if n == 1:
        return 1
    return dfs(n-1) + 1 + dfs(n-1)

print(dfs(3))