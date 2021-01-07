import sys

sys.stdin = open("그리디-모험가 길드.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nlist = sorted(list(map(int, input().split())))
    print(nlist)
    groups = 0
    people = 0
    groupnum = 0
    for e in nlist:
        groupnum = e
        people += 1
        if groupnum == people:
            groups += 1
            groupnum = 0
            people = 0
    print(groups)