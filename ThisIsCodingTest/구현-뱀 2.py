from collections import defaultdict
from collections import deque
import sys

sys.stdin = open("구현-뱀.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Map = [[0] * (N+1) for _ in range(N+1)]
    K = int(input())
    for _ in range(K):
        y, x = map(int, input().split())
        Map[y][x] = 1
    L = int(input())
    TD = defaultdict(int)
    for _ in range(L):
        t, d = input().split()
        t = int(t)
        TD[t] = d
    # print(TD)
    Q = deque()
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    sr, sc, sd = 1, 1, 1
    time = 0
    Map[1][1] = 2
    Q.append((1,1))
    while True:
        time += 1
        sr += dy[sd]
        sc += dx[sd]
        if time in TD:
            if TD[time] == 'L': sd = (sd-1)%4
            elif TD[time] == 'D': sd = (sd+1)%4
        if not(1<=sr<=N) or not(1<=sc<=N): break
        if Map[sr][sc] == 2: break
        if Map[sr][sc] == 1: pass
        elif Map[sr][sc] == 0:
            tr, tc = Q.popleft()
            Map[tr][tc] = 0
        Map[sr][sc] = 2
        Q.append((sr,sc))
    print(time)