from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("10552-DOM-1.txt", "r")

input = sys.stdin.readline

N, M, P = map(int, input().split())

nl = []
hndict = defaultdict(list)
for n in range(N):
    f, h = map(int, input().split())
    nl.append((f,h))
    hndict[h].append(n)

visited = [False] * (M+1)

def dfs(ch, tries):
    if visited[ch]:
        return -1
    visited[ch] = True
    if ch in hndict:
        return dfs(nl[hndict[ch][0]][0], tries + 1)

    return tries

print(dfs(P,0))