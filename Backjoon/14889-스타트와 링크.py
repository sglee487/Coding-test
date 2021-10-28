import sys
sys.setrecursionlimit(10**9)
from itertools import permutations, combinations

sys.stdin = open("14889-스타트와 링크-3.txt", "r")

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

C = set(range(N))


def get_teamscore(team_set, S):
    total = 0
    for i, j in permutations(team_set, 2):
        total += S[i][j]
        total += S[j][j]
    return total


result = 987654321
for comb in combinations(C, N//2):
    result = min(result, abs(get_teamscore(comb,S) - get_teamscore(C-set(comb),S)))

print(result)