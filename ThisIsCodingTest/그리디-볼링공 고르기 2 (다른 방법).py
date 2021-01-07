import sys

sys.stdin = open("그리디-볼링공 고르기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nlist = sorted(list(map(int, input().split())))
    print(nlist)
    countlist = [0] * (M+1)
    for i in range(1,M+1):
        countlist[i] = nlist.count(i)
    print(countlist)
    result = 0
    for e in countlist[1:]:
        N -= e
        result += (N * e)
    print(result)