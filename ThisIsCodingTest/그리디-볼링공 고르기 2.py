import sys

sys.stdin = open("그리디-볼링공 고르기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nlist = sorted(list(map(int, input().split())))
    print(nlist)
    count = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if nlist[i] != nlist[j]:
                count += 1
    print(count)