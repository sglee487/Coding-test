import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("16500-문자열 판별-5.txt", "r")

input = sys.stdin.readline

S = input().strip()
N = int(input())
al = [input().strip() for _ in range(N)]
dp = [[0] * len(S) for _ in range(N)]

def dfs(index, dp, S):
    if index == len(S):
        return True
    for i, a in enumerate(al):
        if index + len(a) > len(S): continue
        if S[index:index + len(a)] == a and dp[i][index] == 0:
            dp[i][index] = 1
            if dfs(index + len(a), dp, S):
                return True

    return False

answer = dfs(0,dp, S)
if answer:
    print(1)
else:
    print(0)