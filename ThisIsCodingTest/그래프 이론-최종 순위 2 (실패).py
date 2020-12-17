import sys

sys.stdin = open("그래프 이론-최종 순위 1.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에
TC = int(input())

for tc in range(TC):
    n = int(input())
    tl = list(map(int, input().split()))
    winnners = [[] for _ in range(n+1)]
    losers = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i < j:
                losers[tl[i]].append(tl[j])
            elif i > j:
                winnners[tl[i]].append(tl[j])
    # print(tl)
    # print(winnners)
    # print(losers)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if tl.index(a) < tl.index(b):
            winnners[b].remove(a)
            losers[a].remove(b)
            winnners[a].append(b)
            losers[b].append(a)
        elif tl.index(a) > tl.index(b):
            winnners[a].remove(b)
            losers[b].remove(a)
            winnners[b].append(a)
            losers[a].append(b)
    # print(winnners)
    # print(losers)

    ctd = False
    imposs = False
    ntl = [0] * (n+1)
    for i in range(1,n+1):
        wc = len(winnners[i])
        lc = len(losers[i])
        wrank = wc+1
        lrank = n-lc
        if wc + lc < n-1:
            ctd = True
            break
        elif wc + lc > n-1:
            imposs = True
            break
        # print(i,wrank,lrank)
        ntl[wrank] = i
    # print(ntl)
    if ntl[1:].count(0) != 0:
        imposs = True
    if len(set(ntl[1:])) != n:
        imposs = True
    if ctd:
        print("?")
    elif imposs:
        print("IMPOSSIBLE")
    else:
        print(ntl[1:])