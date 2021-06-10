import sys
sys.setrecursionlimit(10**9)
from itertools import permutations

sys.stdin = open("14888-연산자 끼워넣기-3.txt", "r")

# input = sys.stdin.readline

N = int(input())

al = list(map(int, input().split()))

opers = list(map(int, input().split()))

answer_max = -9999999999
answer_min = 9999999999

def dfs(step, sum_result):
    global answer_max, answer_min
    if step == N-1:
        answer_min = min(answer_min, sum_result)
        answer_max = max(answer_max, sum_result)
        return sum_result
    if opers[0] > 0:
        opers[0] -= 1
        dfs(step + 1, sum_result + al[step + 1])
        opers[0] += 1
    if opers[1] > 0:
        opers[1] -= 1
        dfs(step + 1, sum_result - al[step + 1])
        opers[1] += 1
    if opers[2] > 0:
        opers[2] -= 1
        dfs(step + 1, sum_result * al[step + 1])
        opers[2] += 1
    if opers[3] > 0:
        if al[step+1] == 0:
            return
        opers[3] -= 1
        # 음수를 양수로 나눌 때
        if sum_result < 0 and al[step+1] > 0:
            sum_result *= -1
            sum_result = sum_result // al[step + 1]
            dfs(step+1, -1*sum_result)
        else:
            dfs(step+1, sum_result // al[step+1])
        opers[3] += 1

dfs(0, al[0])
print(answer_max)
print(answer_min)