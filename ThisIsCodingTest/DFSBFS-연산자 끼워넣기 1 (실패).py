# https://www.acmicpc.net/problem/14888
import sys

sys.stdin = open("DFSBFS-연산자 끼워넣기.txt", "r")

def dfs(cur_num,step):
    global highest, lowest, Numbers, pmmd, N
    if step+1 == N:
        highest = max(highest,cur_num)
        lowest = min(lowest,cur_num)
        # print(cur_num)
        return
    for i, c in enumerate(pmmd):
        if c == 0: continue
        if i == 0:
            pmmd[i] -= 1
            dfs(cur_num + Numbers[step+1],step+1)
            pmmd[i] += 1
        elif i == 1:
            pmmd[i] -= 1
            dfs(cur_num - Numbers[step+1],step+1)
            pmmd[i] += 1
        elif i == 2:
            pmmd[i] -= 1
            dfs(cur_num * Numbers[step+1],step+1)
            pmmd[i] += 1
        elif i == 3:
            if Numbers[step+1] == 0: continue
            pmmd[i] -= 1
            if cur_num < 0:
                dfs((-cur_num) // Numbers[step+1],step+1)
            else:
                dfs(cur_num // Numbers[step+1],step+1)
            pmmd[i] += 1

    return

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N = int(sys.stdin.readline())
    Numbers = list(map(int, sys.stdin.readline().split()))
    pmmd = list(map(int, sys.stdin.readline().split()))
    # print(Numbers,pmmd)
    highest = int(-10e9)
    lowest = int(10e9)
    dfs(Numbers[0],0)
    print(highest)
    print(lowest)
