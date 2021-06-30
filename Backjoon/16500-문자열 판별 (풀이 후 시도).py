import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("16500-문자열 판별-5.txt", "r")

input = sys.stdin.readline

S = input().strip()
N = int(input())
al = [input().strip() for _ in range(N)]
dpo = [0] * len(S)

def dfs(index, dpo, S):
    if index == len(S):
        return True
    if dpo[index] == 1:
        return False # 2. 어 그래
    for i, a in enumerate(al):
        if index + len(a) > len(S): continue
        if S[index:index + len(a)] == a and dpo[index] == 0:
            if dfs(index + len(a), dpo, S):
                return True
    dpo[index] = 1 # 1. 내가 진작 해봤는데 아니더라
    return False

answer = dfs(0,dpo, S)
if answer:
    print(1)
else:
    print(0)