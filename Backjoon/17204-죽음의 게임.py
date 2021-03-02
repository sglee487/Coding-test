import sys

sys.stdin = open("17204-죽음의 게임-2.txt", "r")

input = sys.stdin.readline

N, K = map(int, input().split())
a = []
for _ in range(N):
    a.append(int(input()))
visited = [False] * N
M = 0
now = 0
while True:
    if now == K:
        break
    if visited[now]:
        M = -1
        break
    visited[now] = True
    now = a[now]
    M += 1
print(M)