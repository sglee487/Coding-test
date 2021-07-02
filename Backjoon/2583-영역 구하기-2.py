import sys
sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2583-영역 구하기-1.txt", "r")

input = sys.stdin.readline

M, N, K = map(int, input().split())
maps = [[0] * N for _ in range(M)]
for _ in range(K):
    n1, m1, n2, m2 = map(int, input().split())
    for r in range(m1,m2):
        for c in range(n1,n2):
            maps[r][c] = 1

visited = [[False] * N for _ in range(M)]

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(r, c):
    size = 1
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0<=nr<M and 0<=nc<N): continue
        if maps[nr][nc] != 0 or visited[nr][nc]: continue
        visited[nr][nc] = True
        size += dfs(nr,nc)
    return size

sizel = []
for r in range(M):
    for c in range(N):
        if maps[r][c] == 0 and not visited[r][c]:
            visited[r][c] = True
            sizel.append(dfs(r,c))

print(len(sizel))
sizel.sort()
print(*sizel)