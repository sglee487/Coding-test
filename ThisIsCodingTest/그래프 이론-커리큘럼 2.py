from collections import deque
import sys

sys.stdin = open("그래프 이론-커리큘럼.txt", "r")

N = int(input())

times = [0] * (N+1)
indegree = [0] * (N+1)
nxtgraph = [[] for _ in range(N+1)]

for i in range(1,N+1):
    command = list(map(int, input().split()))
    times[i] = command[0]
    for e in command[1:]:
        if e == -1:
            break
        indegree[i] += 1
        nxtgraph[e].append(i)

print(indegree)
print(nxtgraph)

dp = [0] * (N+1)

Q = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        Q.append(i)

while Q:
    now = Q.popleft()
    print(now)
    dp[now] = dp[now] + times[now]
    for nxt in nxtgraph[now]:
        indegree[nxt] -= 1
        dp[nxt] = max(dp[now],dp[nxt])
        if indegree[nxt] == 0:
            Q.append(nxt)

print(dp)