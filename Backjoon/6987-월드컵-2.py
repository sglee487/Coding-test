# -*- coding: utf-8 -*-
import copy
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("6987-월드컵-1.txt", "r")

fights = list(combinations([0,1,2,3,4,5],2))

input = sys.stdin.readline

def dfs(round, teams):
    if round == 15:
        return not any(map(any, teams))

    team1 = fights[round][0]
    team2 = fights[round][1]

    ret = False

    if teams[team1][0] and teams[team2][2]:
        teams[team1][0] -= 1
        teams[team2][2] -= 1
        ret = ret or dfs(round+1, teams)
        teams[team1][0] += 1
        teams[team2][2] += 1

    if teams[team1][1] and teams[team2][1]:
        teams[team1][1] -= 1
        teams[team2][1] -= 1
        ret = ret or dfs(round+1, teams)
        teams[team1][1] += 1
        teams[team2][1] += 1

    if teams[team1][2] and teams[team2][0]:
        teams[team1][2] -= 1
        teams[team2][0] -= 1
        ret = ret or dfs(round+1, teams)
        teams[team1][2] += 1
        teams[team2][0] += 1

    return ret


TEST_CASES = 4
answer = []
for _ in range(TEST_CASES):
    T = list(map(int, input().split()))
    teams = []
    for i in range(0,len(T),3):
        teams.append(T[i:i+3])
    answer.append(int(dfs(0, teams)))

print(*answer)