import sys
from collections import deque
import copy

sys.stdin = open("2020년 상반기 삼성전자-청소년 상어.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에

# https://github.com/ndb796/python-for-coding-test/blob/master/19/2.py

# 위 위왼 왼 왼아래 아래 아래오 오 오위
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]

def find_fish(water,i):
    for r in range(4):
        for c in range(4):
            if water[r][c][0] == i:
                return r, c
    return None


def change_fishes(water,sr,sc):
    for i in range(1,17):
        position = find_fish(water,i)
        if position != None:
            ir, ic = position[0], position[1]
            for j in range(8):
                id = (water[ir][ic][1]+j)%8
                nir, nic = ir + dy[id], ic + dx[id]
                if not(0<=nir<4 and 0<=nic<4): continue
                if (nir,nic) == (sr,sc): continue
                water[ir][ic][1] = id
                water[ir][ic], water[nir][nic] = water[nir][nic], water[ir][ic]
                break


T = int(input())
for test_case in range(1, T + 1):
    water = [[None] * 4 for _ in range(4)]

    for i in range(4):
        a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
        water[i][0] = [a1,b1-1]
        water[i][1] = [a2, b2 - 1]
        water[i][2] = [a3, b3 - 1]
        water[i][3] = [a4, b4 - 1]
    # print(*water,sep='\n')

    Q = deque()
    Q.append((0,0,water[0][0][0],copy.deepcopy(water)))
    result = 0
    while Q:
        sr, sc, total, copyedwater = Q.popleft()
        result = max(total,result)
        sd = copyedwater[sr][sc][1]
        copyedwater[sr][sc] = [0,'x']

        change_fishes(copyedwater,sr,sc)

        nsr, nsc = sr+dy[sd], sc+dx[sd]
        while 0<=nsr<4 and 0<=nsc<4:
            if copyedwater[nsr][nsc][0] != 0:
                Q.append((nsr,nsc, total + copyedwater[nsr][nsc][0],copy.deepcopy(copyedwater)))
            nsr, nsc = nsr + dy[sd], nsc + dx[sd]
    print(result)