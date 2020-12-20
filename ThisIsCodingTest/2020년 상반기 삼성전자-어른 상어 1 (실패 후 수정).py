import sys

sys.stdin = open("2020년 상반기 삼성전자-어른 상어.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에

# 위 아래 왼쪽 오른쪽
dy = [-1,1,0,0]
dx = [0,0,-1,1]
# https://github.com/ndb796/python-for-coding-test/blob/master/19/3.py

def smellupdate(water,smell):
    for r in range(N):
        for c in range(N):
            if water[r][c] != 0:
                smell[r][c] = [water[r][c],k]
            else:
                smell[r][c][1] -= 1
                if smell[r][c][1] == 0:
                    smell[r][c] = [0,0]
    return

def sharkupdate(water,sharkdl,smell):
    newwater = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if water[r][c] != 0:
                sharknum = water[r][c]
                d = sharkdl[sharknum]
                moved = False
                for i in range(4):
                    nr, nc = r + dy[priority[sharknum][d][i]], c + dx[priority[sharknum][d][i]]
                    if not (0<=nr<N and 0<=nc<N): continue
                    if smell[nr][nc][0] != 0: continue
                    if newwater[nr][nc] != 0:
                        newwater[nr][nc] = min(newwater[nr][nc],sharknum)
                    else:
                        newwater[nr][nc] = sharknum
                    sharkdl[sharknum] = priority[sharknum][d][i]
                    moved = True
                    break
                if not moved:
                    for i in range(4):
                        nr, nc = r + dy[priority[sharknum][d][i]], c + dx[priority[sharknum][d][i]]
                        if not (0 <= nr < N and 0 <= nc < N): continue
                        if smell[nr][nc][0] != sharknum: continue
                        newwater[nr][nc] = sharknum
                        sharkdl[sharknum] = priority[sharknum][d][i]
                        break


    return newwater

T = int(input())
for test_case in range(1, T + 1):
    N, M, k = map(int, input().split())
    water = [list(map(int, input().split())) for _ in range(N)]
    smell = [[None] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if water[r][c] != 0:
                smell[r][c] = [water[r][c],k]
            else:
                smell[r][c] = [0,0]

    sharkdl = [0] + list(map(lambda x:int(x)-1, input().split()))
    priority = [[] for _ in range(M+1)]
    for i in range(1,M+1):
        for j in range(4):
            priority[i].append(list(map(lambda x:int(x)-1, input().split())))
    # print(*water,sep='\n')
    # print(*smell,sep='\n')
    # print()
    time = 0
    while True:
        water = sharkupdate(water,sharkdl,smell)
        smellupdate(water,smell)
        time += 1
        onlyone = True
        for r in range(N):
            for c in range(N):
                if water[r][c] > 1:
                    onlyone = False
                    break
        if onlyone:
            print(time)
            break
        else:
            if time >= 1000:
                print(-1)
                break
        # print(*water, sep='\n')
        # print(*smell, sep='\n')
        # print()