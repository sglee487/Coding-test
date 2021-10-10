import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("14716-현수막-1.txt", "r")

input = sys.stdin.readline

M, N = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(M)]

def dfs(r, c, picture, visited, count_gul):
    # 위 위오 오 오아 아 아왼 왼 왼위
    dy = [-1, -1, 0, 1, 1, +1, +0, -1]
    dx = [+0, +1, 1, 1, 0, -1, -1, -1]

    for i in range(8):
        nr, nc = r + dy[i], c + dx[i]
        if not (0<=nr<M and 0<=nc<N): continue
        if picture[nr][nc] == 0 or visited[nr][nc]: continue
        visited[nr][nc] = count_gul
        dfs(nr,nc,picture,visited, count_gul)

def search_picture(picture):
    global M, N
    count_gul = 1
    visited = [[0 for _ in range(N)] for _ in range(M)]

    for r in range(M):
        for c in range(N):
            if picture[r][c] == 1 and not visited[r][c]:
                visited[r][c] = count_gul
                dfs(r, c, picture, visited, count_gul)
                count_gul += 1

    # print(*visited, sep='\n')

    return count_gul - 1

print(search_picture(picture))