import sys
sys.setrecursionlimit(10000)

sys.stdin = open("1520-내리막 길-1.txt", "r")

input = sys.stdin.readline

M, N = map(int, input().split())
Matrix = []
for _ in range(M):
    Matrix.append(list(map(int, input().split())))

dp = [[-1] * N for _ in range(M)]

dp[M-1][N-1] = 1

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(r,c):
    if dp[r][c] != -1:
        return dp[r][c]

    ways = 0
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if (0<=nr<M and 0<=nc<N) and (Matrix[nr][nc] < Matrix[r][c]):
            ways += dfs(nr,nc)
    dp[r][c] = ways

    return dp[r][c]

dfs(0,0)

# print(*dp,sep='\n')
print(dp[0][0])