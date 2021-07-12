from collections import deque
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("1525-퍼즐-6.txt", "r")

input = sys.stdin.readline

def m2l(matrix):
    num = 0
    index = -1
    for r in range(3):
        for c in range(3):
            if matrix[r][c] == 0:
                index = (3*r) + c
            num += (matrix[r][c] * ((1000 ** r ) * (10 ** c)))
    return num, index

def swap(now, i, j):
    num = now
    nj = now % (10 ** (j+1)) // (10 ** (j))
    num -= (nj * (10 ** j))
    num += (nj * (10 ** i))
    return num

def bfs(matrix):
    dp = set()
    start, zi = m2l(matrix)
    goal = 87654321
    Q = deque()
    Q.append((start, zi, 0))
    dp.add(start)
    while Q:
        now, i, d = Q.popleft()
        if now == goal:
            return d
        # 행렬 기준
        # 오른쪽으로
        if i%3 != 2 and i+1 < 9:
            num = swap(now, i, i+1)
            if num not in dp:
                dp.add(num)
                Q.append((num, i+1, d+1))
        # 왼쪽으로
        if i%3 != 0 and i-1>=0:
            num = swap(now, i, i-1)
            if num not in dp:
                dp.add(num)
                Q.append((num, i-1, d+1))
        # 위쪽으로
        if i-3 >= 0:
            num = swap(now, i, i-3)
            if num not in dp:
                dp.add(num)
                Q.append((num, i-3, d+1))
        # 아래쪽으로
        if i+3 < 9:
            num = swap(now, i, i+3)
            if num not in dp:
                dp.add(num)
                Q.append((num, i+3, d+1))


    return -1

matrix = [list(map(int, input().split())) for _ in range(3)]

print(bfs(matrix))