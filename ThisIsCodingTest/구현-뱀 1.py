from collections import defaultdict
from collections import deque
import sys

sys.stdin = open("구현-뱀2.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [[0] * (N+1) for _ in range(N+1)]
    APN = int(input())
    for _ in range(APN):
        r, c = map(int, input().split())
        board[r][c] = 1
    # print(*board, sep='\n')
    ACN = int(input())
    MD = defaultdict(str)
    for _ in range(ACN):
        t, a = input().split()
        MD[int(t)] = a
    # print(MD)
    # 위, 오른쪽, 아래, 왼쪽
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    now_r, now_c = 1, 1
    now_d = 1
    now_t = 0
    havingbody = deque()
    havingbody.append((1,1))
    while now_t < 10000:
        now_t += 1
        next_r, next_c = now_r + dy[now_d], now_c + dx[now_d]
        if not(1<=next_r<=N) or not(1<=next_c<=N): break
        if (next_r,next_c) in havingbody: break
        if board[next_r][next_c] == 0:
            havingbody.popleft()
        if board[next_r][next_c] == 1:
            board[next_r][next_c] = 0
        havingbody.append((next_r,next_c))
        if now_t in MD:
            if MD[now_t] == 'L':
                now_d = (now_d - 1) % 4
            if MD[now_t] == 'D':
                now_d = (now_d + 1) % 4
        now_r, now_c = next_r, next_c

    print(now_t)
