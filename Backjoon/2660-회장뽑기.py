from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2660-회장뽑기-2.txt", "r")

input = sys.stdin.readline

N = int(input())
graph = [[] * (N+1) for _ in range(N+1)]
while True:
    a, b = map(int,input().split())
    if a == -1: break
    graph[a].append(b)
    graph[b].append(a)

friend_list = [int(10e9)] * (N+1)

def get_dist(iam):
    dists = [-1] * (N+1)
    Q = deque(graph[iam])
    dist = 1
    while Q:
        now_len = len(Q)
        # print(Q, now_len)
        for _ in range(now_len):
            friend = Q.popleft()
            if dists[friend] != -1: continue
            dists[friend] = dist
            for child in graph[friend]:
                if dists[child] == -1 and child != iam:
                    Q.append(child)
        dist += 1
    return dists

have_list = [int(10e9)] * (N+1)
for i in range(1, N+1):
    # print(i, get_dist(i))
    max_score = max(get_dist(i))
    if max_score == -1:
        have_list[i] = int(10e9)
    else:
        have_list[i] = max_score

# print(have_list)
min_have = min(have_list)
candidates = [i for i, h in enumerate(have_list) if h == min_have]
print(min_have, len(candidates))
print(*candidates, sep=' ')
