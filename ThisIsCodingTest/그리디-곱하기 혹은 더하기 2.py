import sys

sys.stdin = open("그리디-곱하기 혹은 더하기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    nlist = list(map(int, input()))
    print(nlist)
    totalnum = nlist[0]
    for e in nlist[1:]:
        if totalnum <= 1 or e <= 1:
            totalnum = totalnum + e
        else:
            totalnum = totalnum * e
    print(totalnum)