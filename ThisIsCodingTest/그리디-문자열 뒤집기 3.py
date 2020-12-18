import sys

sys.stdin = open("그리디-문자열 뒤집기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    nl = list(map(int,input()))
    # print(nl)
    tz = 0
    to = 0
    if nl[0] == 0:
        to += 1
    else:
        tz += 1
    N = len(nl)
    for i in range(N-1):
        if nl[i] == 0 and nl[i+1] == 1:
            tz += 1
        if nl[i] == 1 and nl[i+1] == 0:
            to += 1
    print(min(tz,to))