import sys
from itertools import combinations

sys.setrecursionlimit(10**9)


sys.stdin = open("14889-스타트와 링크-3.txt", "r")

input = sys.stdin.readline

N = int(input())
M = N//2
S = [list(map(int, input().split())) for _ in range(N)]
SD = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        SD[min(i,j)][max(i,j)] += S[i][j]

all_set = set(range(N))

def get_team_sum(team):
    ret = 0
    for comb in combinations(team,2):
        one, two = comb[0], comb[1]
        ret += SD[one][two]
    return ret

answer = 987654321

for comb in combinations(range(N), M):
    team1 = comb
    team2 = tuple(all_set - set(comb))
    if team1 == team2: break
    answer = min(answer, abs(get_team_sum(team1) - get_team_sum(team2)))

print(answer)