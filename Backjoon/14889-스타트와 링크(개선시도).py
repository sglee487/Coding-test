import sys
sys.setrecursionlimit(10**9)
from itertools import combinations

sys.stdin = open("14889-스타트와 링크-2.txt", "r")

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

C = set(range(N))

comb = list(combinations(C, N//2))

results = []
for i in range(len(comb) // 2):
    A = 0
    B = 0
    for p1, p2 in combinations(comb[i], 2):
        A += S[p1][p2] + S[p2][p1]
    for p1, p2 in combinations(C-set(comb[i]),2):
        B += S[p1][p2] + S[p2][p1]
    results.append(abs(A-B))


print(min(results))