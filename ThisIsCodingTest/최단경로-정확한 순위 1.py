import sys
from collections import defaultdict

sys.stdin = open("최단경로-정확한 순위.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    winners = defaultdict(set)
    losers = defaultdict(set)
    for _ in range(M):
        w, l = map(int, input().split())
        losers[w].add(l)
        winners[l].add(w)
    for i in range(1, N+1):
        for loser in losers[i]:
            winners[loser].update(winners[i])
        for winner in winners[i]:
            losers[winner].update(losers[i])

    count = 0
    for i in range(1, N+1):
        if len(winners[i]) + len(losers[i]) == N-1:
            count += 1
    print(count)