import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("14500-테트로미노-2.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dlur = [((0,0),(0,1),(0,2),(1,1)),
        ((1,0),(0,1),(1,1),(2,1)),
        ((0,1),(1,0),(1,1),(1,2)),
        ((0,0),(1,0),(2,0),(1,1))]

result = -1

def dfs(step, now_r, now_c, cur_sum):
    global result, N, M, board, visited
    if step == 3:
        result = max(result, cur_sum)
        return

    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    for i in range(4):
        nxt_r, nxt_c = now_r + dy[i], now_c + dx[i]
        if not (0<= nxt_r < N and 0 <= nxt_c < M): continue
        if visited[nxt_r][nxt_c]: continue
        visited[nxt_r][nxt_c] = True
        dfs(step+1, nxt_r, nxt_c, cur_sum + board[nxt_r][nxt_c])
        visited[nxt_r][nxt_c] = False

def for_dlur(now_r, now_c):
    global result, N, M, board, dlur
    for bu in dlur:
        if (0<= now_r + bu[0][0] < N and 0<= now_c + bu[0][1] < M) \
            and (0<= now_r + bu[1][0] < N and 0<= now_c + bu[1][1] < M) \
            and (0<= now_r + bu[2][0] < N and 0<= now_c + bu[2][1] < M) \
            and (0<= now_r + bu[3][0] < N and 0<= now_c + bu[3][1] < M) :
            alsum = board[now_r + bu[0][0]][now_c + bu[0][1]] \
            + board[now_r + bu[1][0]][now_c + bu[1][1]] \
            + board[now_r + bu[2][0]][now_c + bu[2][1]] \
            + board[now_r + bu[3][0]][now_c + bu[3][1]]
            result = max(result, alsum)


for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(0, r, c, board[r][c])
        for_dlur(r,c)
        visited[r][c] = False

print(result)