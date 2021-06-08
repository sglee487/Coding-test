import sys
sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2583-영역 구하기-1.txt", "r")

input = sys.stdin.readline

M, N, K = map(int, input().split())

matrix = [[0] * M for _ in range(N)]
nemos = list(tuple(map(int, input().split())) for _ in range(K))
# nemos = []
# for _ in range(K):
#     nemo = tuple(map(int, input().split()))
#     nemos.append(nemo)


def drow(r1, c1, r2, c2, matrix):
    for r in range(r1, r2):
        for c in range(c1, c2):
            matrix[r][c] = 1


def check(r, c, dp):
    if dp[r][c]:
        return False


for r1, c1, r2, c2 in nemos:
    drow(r1,c1,r2,c2,matrix)

def dfs(r, c, count, step, matrix):
    matrix[r][c] = count + 2
    step += 1
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if 0<=nr<N and 0<=nc<M and matrix[nr][nc] == 0:
            step = dfs(nr,nc,count,step, matrix)

    return step

count = 0
result = []
def check(r, c, matrix):
    global count
    if matrix[r][c]:
        return False
    matrix[r][c] = count + 2
    count += 1
    step = dfs(r,c,count, 0, matrix)
    result.append(step)


for r in range(N):
    for c in range(M):
        check(r,c,matrix)

print(count)
print(*sorted(result))