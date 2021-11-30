# -*- coding: utf-8 -*-
import copy
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2469-사다리 타기-1.txt", "r")

input = sys.stdin.readline

K = int(input())
N = int(input())


def chr2ord(chr):
    return int(ord(chr)-65)

expect = list(map(chr2ord, input().strip()))
# expect = list(input().strip())

ladder = [input().strip() for _ in range(N)]
ladder_reverse = ladder[::-1]
QR = -1
for r in range(N):
    if ladder_reverse[r][0] == '?':
        QR = r
        break

to_mid = list(range(K))
to_end = list(range(K))


def make_changer(changer, changee):
    for c in range(len(changer)):
        if changer[c] == '-':
            changee[c], changee[c + 1] = changee[c + 1], changee[c]
    return


def change_order(changer, changee):
    new_list = [-1] * K
    for i in range(K):
        new_list[i] = changee[changer[i]]
    return new_list


for r in range(QR):
    make_changer(ladder_reverse[r], to_mid)

for r in range(QR+1,N):
    make_changer(ladder_reverse[r], to_end)

answer = []

candidates_middle = ['*' for _ in range(K-1)]
def create_middle(step):
    global answer
    if step >= K-1:
        temp = list(range(K))
        make_changer(candidates_middle, temp)
        result = expect[:]
        result = change_order(to_mid, result)
        result = change_order(temp, result)
        result = change_order(to_end, result)
        if result == list(range(K)):
            answer = candidates_middle[:]
        return
    candidates_middle[step] = '-'
    create_middle(step+2)
    candidates_middle[step] = '*'
    create_middle(step+1)
    return

create_middle(0)

if answer:
    print(''.join(answer))
else:
    print('x' * (K-1))