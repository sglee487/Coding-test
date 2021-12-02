# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2641-다각형그리기-1.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))
M = int(input())
ml = [list(map(int, input().split())) for _ in range(M)]

reverse_dict = {1:3,2:4,3:1,4:2}

nlnl = nl + nl
nlnlr = [reverse_dict[e] for e in nlnl][::-1]

answers = []

def check(i):
    global nlnl, nlnlr, answers
    for j in range(2*N-1):
        if nlnl[j:j+N] == ml[i]:
            answers.append(i)
            return True
        if nlnlr[j:j+N] == ml[i]:
            answers.append(i)
            return True

    return False

for i in range(M):
    check(i)

print(len(answers))
if answers:
    for ei in answers:
        print(*ml[ei])