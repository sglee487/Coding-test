# https://www.acmicpc.net/problem/14888
import sys

sys.stdin = open("DFSBFS-연산자 끼워넣기.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에

def dfs(step,totalsum):
    global maxvalue, minvalue, N, nlist, pmmd
    if step == N:
        maxvalue = max(maxvalue,totalsum)
        minvalue = min(minvalue,totalsum)
    else:
        if pmmd[0] > 0:
            pmmd[0] -= 1
            dfs(step+1,totalsum + nlist[step])
            pmmd[0] += 1
        if pmmd[1] > 0:
            pmmd[1] -= 1
            dfs(step+1,totalsum - nlist[step])
            pmmd[1] += 1
        if pmmd[2] > 0:
            pmmd[2] -= 1
            dfs(step+1,totalsum * nlist[step])
            pmmd[2] += 1
        if pmmd[3] > 0 and nlist[step] != 0:
            pmmd[3] -= 1
            if totalsum < 0:
                dfs(step + 1, -(-totalsum // nlist[step]))
            else:
                dfs(step+1,totalsum // nlist[step])
            pmmd[3] += 1



T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N = int(input())
    nlist = list(map(int, input().split()))
    pmmd = list(map(int, input().split()))
    maxvalue = -int(10e9)
    minvalue = int(10e9)
    # print(pmmd)
    dfs(1,nlist[0])
    print(maxvalue)
    print(minvalue)