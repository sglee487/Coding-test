from collections import deque
import sys

sys.stdin = open("DFSBFS-경쟁적 전염.txt", "r")

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]
    S, R, C = map(int, input().split())
    Q = []
    for r in range(N):
        for c in range(N):
            if lab[r][c] != 0:
                Q.append((lab[r][c],0,r,c))

    Q.sort()
    Q = deque(Q)
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    while Q:
        virus, t, r, c = Q.popleft()
        if t == S: break
        for i in range(4):
            nr, nc = r + dy[i], c+dx[i]
            if (0<=nr<N) and (0<=nc<N):
                if lab[nr][nc] == 0:
                    lab[nr][nc] = virus
                    Q.append((virus,t+1,nr,nc))
    print(*lab,sep='\n')
    print(lab[R-1][C-1])