import sys

sys.stdin = open('구현-왕실의 나이트-1.txt', 'r')

input = sys.stdin.readline

# 위왼 위오 오위 오아 아오 아왼 왼아 왼위
dy = [-2, -2, -1, 1, 2, 2, -1, 1]
dx = [-1, 1, 2, 2, 1, -1, -2, -2]

nd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

r, c = input()
r = nd[r]
c = int(c) - 1

N = 8
answer = 0
for i in range(8):
    nr, nc = r + dy[i], c + dx[i]
    if (0<=nr < N and 0<=nc<N): answer += 1

print(answer)