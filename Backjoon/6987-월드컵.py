# -*- coding: utf-8 -*-
import copy
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("6987-월드컵-1.txt", "r")

input = sys.stdin.readline

leaderboard = [[0] * 3 for _ in range(6)]

fights = list(combinations([0,1,2,3,4,5],2))

possible_list = []

result = bool()

def backtrack(count, teaml):
    global result
    if count == 15:
        for i in range(6):
            if not teaml[i] == [0,0,0]:
                return
        result = True
        return

    team1 = fights[count][0]
    team2 = fights[count][1]

    if teaml[team1][0] and teaml[team2][2]:
        teaml[team1][0] -= 1
        teaml[team2][2] -= 1
        backtrack(count+1, teaml)
        teaml[team1][0] += 1
        teaml[team2][2] += 1

    if teaml[team1][1] and teaml[team2][1]:
        teaml[team1][1] -= 1
        teaml[team2][1] -= 1
        backtrack(count+1, teaml)
        teaml[team1][1] += 1
        teaml[team2][1] += 1

    if teaml[team1][2] and teaml[team2][0]:
        teaml[team1][2] -= 1
        teaml[team2][0] -= 1
        backtrack(count+1, teaml)
        teaml[team1][2] += 1
        teaml[team2][0] += 1


    return

test_all_list = list(list(map(int, input().split())) for _ in range(4))

for test_case in range(4):
    teaml = []
    for i in range(6):
        teaml.append(test_all_list[test_case][i*3:(i+1)*3])
    result = False
    backtrack(0, teaml)
    if result:
        print(1)
    else:
        print(0)