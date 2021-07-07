from collections import deque
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("7562-나이트의 이동-1.txt", "r")

def bfs(Q, goal):
    global l, board
    # 오위위 오위오 오아오 오아아 왼아아 왼아왼 왼오왼 왼오오
    dy = [-2,-1,1,2,2,1,-1,-2]
    dx = [1,2,2,1,-1,-2,-2,-1]
    while Q:
        r, c = Q.popleft()
        for i in range(8):
            nr, nc = r + dy[i], c + dx[i]
            if not (0<=nr<l and 0<=nc<l): continue
            if board[nr][nc] != 0: continue
            board[nr][nc] = board[r][c] + 1
            Q.append((nr,nc))
            if (nr,nc) == (goal):
                return board[nr][nc]

    return 0

input = sys.stdin.readline
T = int(input())
for test_case in range(T):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    if start == goal:
        print(0)
        continue
    Q = deque()
    Q.append(start)
    board[start[0]][start[1]] = 0
    print(bfs(Q, goal))