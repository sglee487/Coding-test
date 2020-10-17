from collections import deque
import sys
import copy

sys.stdin = open("DFSBFS-인구 이동.txt", "r")

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, L, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # print(*A, sep='\n')
    result = 0
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    calculated = [[False] * N for _ in range(N)]
    while True:
        change = False
        A_temp = copy.deepcopy(A)
        for r in range(N):
            for c in range(N):
                if calculated[r][c]: continue
                Q = deque()
                Q.append((r,c))
                unionset = set()
                while Q:
                    r, c = Q.pop()
                    if calculated[r][c] : continue
                    calculated[r][c] = True
                    unionset.add((r,c))
                    for i in range(4):
                        nr, nc = r + dy[i], c + dx[i]
                        if not (0 <= nr < N and 0 <= nc < N): continue
                        if L <= abs(A[r][c] - A[nr][nc]) <= R:
                            Q.append((nr,nc))
                            change = True

                if not unionset: break
                unionsum = 0
                for r, c in unionset:
                    unionsum += A[r][c]
                for r, c in unionset:
                    A_temp[r][c] = (unionsum // len(unionset))
        if not change: break
        A = A_temp
        result += 1
        calculated = [[False] * N for _ in range(N)]
        # print(*A, sep='\n')

    print(result)
