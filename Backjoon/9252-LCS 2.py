import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("9252-LCS 2-1.txt", "r")

input = sys.stdin.readline

A = input().strip()
B = input().strip()
N = len(A)
M = len(B)
dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

answerrl = []
r, c = N, M
while r != 0 and c != 0:
    if dp[r][c] == dp[r][c-1]:
        c -= 1
    elif dp[r][c] == dp[r-1][c]:
        r -= 1
    else:
        answerrl.append(A[r-1])
        r -= 1
        c -= 1
print(dp[N][M])
print(''.join(answerrl[::-1]))