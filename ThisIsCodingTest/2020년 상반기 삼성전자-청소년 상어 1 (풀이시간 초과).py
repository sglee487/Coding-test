import sys
from collections import deque
import copy

sys.stdin = open("2020년 상반기 삼성전자-청소년 상어.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에

def find_fishes(water):
    empty = True
    fishes = [[] for _ in range(17)]
    for r in range(4):
        for c in range(4):
            if water[r][c] == 0: continue
            fishes[water[r][c]] = [r,c]
            empty = False
    if empty:
        return None
    else:
        return fishes


T = int(input())
for test_case in range(1, T + 1):
    water = [[0] * 4 for _ in range(4)]
    directions = [[0] * 4 for _ in range(4)]
    # 오른위 위 위왼 왼 왼아래 아래 오른아래 오른 오른위
    dy = [-1,-1,-1,0,1,1,1,0,-1]
    dx = [1,0,-1,-1,-1,0,1,1,1]
    for i in range(4):
        a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
        water[i][0], directions[i][0] = a1, (b1%8)
        water[i][1], directions[i][1] = a2, (b2%8)
        water[i][2], directions[i][2] = a3, (b3%8)
        water[i][3], directions[i][3] = a4, (b4%8)
    fishes = find_fishes(water)
    Q = deque()
    Q.append((0,0,directions[0][0],copy.deepcopy(water),copy.deepcopy(directions),water[0][0]))
    result = 0
    while Q:
        sr, sc, sd, copyedwater, copyeddirections, total = Q.popleft()
        result = max(result, total)
        copyedwater[sr][sc] = 0
        copyeddirections[sr][sc] = 'x'
        fishes = find_fishes(copyedwater)
        if fishes == None: continue
        for fishindex in range(1,17):
            if fishes[fishindex] == []: continue
            fr, fc = fishes[fishindex][0], fishes[fishindex][1]
            for i in range(8):
                nfd = (copyeddirections[fr][fc]+i)%8
                nfr, nfc = fr + dy[nfd] , fc + dx[nfd]
                if not (0<=nfr<4 and 0<=nfc<4): continue
                if (nfr,nfc) == (sr,sc): continue
                fishes[fishindex], fishes[copyedwater[nfr][nfc]] = fishes[copyedwater[nfr][nfc]], fishes[fishindex]
                copyedwater[nfr][nfc], copyedwater[fr][fc] = copyedwater[fr][fc], copyedwater[nfr][nfc]
                copyeddirections[nfr][nfc], copyeddirections[fr][fc] = nfd, copyeddirections[nfr][nfc]
                break
        nsr, nsc = sr + dy[sd], sc + dx[sd]
        while 0<= nsr < 4 and 0<=nsc<4:
            if copyedwater[nsr][nsc] != 0:
                Q.append((nsr,nsc,copyeddirections[nsr][nsc],copy.deepcopy(copyedwater),copy.deepcopy(copyeddirections),total + copyedwater[nsr][nsc]))
            nsr, nsc = nsr + dy[sd], nsc + dx[sd]
    print(result)
    # print("======")