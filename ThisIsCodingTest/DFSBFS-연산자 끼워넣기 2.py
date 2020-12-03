# https://www.acmicpc.net/problem/14888
import sys

sys.stdin = open("DFSBFS-연산자 끼워넣기.txt", "r")

def dfs(index,result,pmmd):
    global N, highest, lowest, Numbers
    if index == N:
        highest = max(result,highest)
        lowest = min(result,lowest)
        return
    else:
        if pmmd[0] > 0:
            pmmd[0] -= 1
            dfs(index+1,result + Numbers[index], pmmd[:])
            pmmd[0] += 1
        if pmmd[1] > 0:
            pmmd[1] -= 1
            dfs(index+1,result - Numbers[index], pmmd[:])
            pmmd[1] += 1
        if pmmd[2] > 0:
            pmmd[2] -= 1
            dfs(index+1,result * Numbers[index], pmmd[:])
            pmmd[2] += 1
        if pmmd[3] > 0 and Numbers[index] != 0:
            pmmd[3] -= 1
            if result < 0:
                dfs(index + 1, -((-result) // Numbers[index]), pmmd[:])
            else:
                dfs(index + 1, result // Numbers[index], pmmd[:])
            pmmd[3] += 1

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N = int(sys.stdin.readline())
    Numbers = list(map(int, sys.stdin.readline().split()))
    pmmd = list(map(int, sys.stdin.readline().split()))
    # print(Numbers,pmmd)
    highest = int(-10e9)
    lowest = int(10e9)
    dfs(1,Numbers[0],pmmd[:])
    print(highest)
    print(lowest)