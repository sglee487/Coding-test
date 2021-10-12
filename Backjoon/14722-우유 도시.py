import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("14722-우유 도시-15.txt", "r")

input = sys.stdin.readline

# https://looview.tistory.com/6
N = int(input())
village = [list(map(int, input().split())) for _ in range(N)]
dp = [[[-1] * 3 for _ in range(N)] for _ in range(N)]

# 오 아래
dy = [0,1]
dx = [1,0]


def dfs(r,c,now):
    if dp[r][c][now] != -1:
        return dp[r][c][now]
    dp[r][c][now] = 0
    for i in range(2):
        nr, nc = r + dy[i], c + dx[i]
        if not (0 <= nr < N and 0 <= nc < N): continue
        if village[nr][nc] == (now+1)%3:
            dp[r][c][now] = max(dp[r][c][now], dfs(nr,nc,(now+1)%3)+1)
        else:
            dp[r][c][now] = max(dp[r][c][now], dfs(nr, nc, now))

    return dp[r][c][now]

if village[0][0] == 0:
    print(dfs(0,0,0)+1)
else:
    print(dfs(0,0,2))

# print(*village, sep='\n')
# print(*dp, sep='\n')