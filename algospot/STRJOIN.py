import heapq
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("STRJOIN-1.txt", "r")

input = sys.stdin.readline


C = int(input())
for _ in range(C):
    n = int(input())
    nl = list(map(int, input().split()))
    if len(nl) == 1:
        print(nl[0])
        continue
    hq = []
    for e in nl:
        heapq.heappush(hq, e)
    answer = 0
    while len(hq) >= 2:
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        answer += a+b
        heapq.heappush(hq, a+b)
    print(answer)