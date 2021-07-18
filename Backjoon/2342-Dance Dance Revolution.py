import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("2342-Dance Dance Revolution-1.txt", "r")

def cal_diff(arrow, foot):
    if foot == 0:
        return 2
    if foot == arrow:
        return 1
    if foot == 1 and arrow == 3:
        return 4
    if foot == 2 and arrow == 4:
        return 4
    if foot == 3 and arrow == 1:
        return 4
    if foot == 4 and arrow == 2:
        return 4
    return 3

def dfs(step, lf, rf):
    global dp, al
    target = al[step]
    if target == 0:
        return 0
    if dp[step][lf][rf] != -1:
        return dp[step][lf][rf]
    lfdif = cal_diff(target, lf)
    rfdif = cal_diff(target, rf)
    lr = dfs(step+1, target, rf) + lfdif
    rr = dfs(step+1, lf, target) + rfdif
    dp[step][lf][rf] = min(lr, rr)

    return dp[step][lf][rf]


input = sys.stdin.readline
al = list(map(int, input().split()))
N = len(al)
dp = [[[-1] * 5 for _ in range(5)] for _ in range(N)]
print(dfs(0, 0, 0))