from collections import deque
import sys

sys.stdin = open("DFSBFS-경쟁적 전염.txt", "r")

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]
    S, R, C = map(int, input().split())
    Qs = [deque() for _ in range(K+1)]
    for r in range(N):
        for c in range(N):
            if lab[r][c] != 0:
                Qs[lab[r][c]].append((r,c,0))
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    labg = [[0] * (N) for _ in range(N)]
    time = 0
    while time <= S:
        for k in range(1,K+1):
            while Qs[k] and time == Qs[k][0][2]:
                r, c, t = Qs[k].popleft()
                if labg[r][c] == 0:
                    labg[r][c] = k
                    for i in range(4):
                        nr, nc = r+dy[i],c+dx[i]
                        if (0<=nr<N) and (0<=nc<N) and labg[nr][nc] == 0:
                            Qs[k].append((nr,nc,t+1))
            # print(*labg, sep='\n')
            # print(Qs)
        time += 1
    # print(*labg,sep='\n')
    print(labg[R-1][C-1])