from collections import deque
from collections import defaultdict
import sys

sys.stdin = open("구현-뱀.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [[1] * (N+2) for _ in range(N+2)]
    for i in range(1,N+1):
        for j in range(1, N+1):
            board[i][j] = 0

    K = int(input())
    for _ in range(K):
        r, c = map(int, input().split())
        board[r][c] = 2

    turndict = defaultdict(int)
    L = int(input())
    for _ in range(L):
        t, d  = input().split()
        turndict[int(t)] = d

    # print(*board,sep='\n')
    # print(turndict)

    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    Bodys = deque()
    Bodys.append((1,1))
    board[1][1] = 3
    Dir = 1
    time = 0
    while True:
        time += 1
        prevheadr, prevheadc = Bodys[-1]
        headr, headc = prevheadr + dy[Dir], prevheadc + dx[Dir]
        if board[headr][headc] == 2:
            pass
        elif board[headr][headc] == 0:
            tailr, tailc = Bodys.popleft()
            board[tailr][tailc] = 0
        elif board[headr][headc] == 3:
            break
        elif board[headr][headc] == 1:
            break
        board[headr][headc] = 3
        Bodys.append((headr,headc))
        if time in turndict:
            if turndict[time] == 'L':
                Dir = (Dir-1) % 4
            elif turndict[time] == 'D':
                Dir = (Dir+1) % 4
    print(time)