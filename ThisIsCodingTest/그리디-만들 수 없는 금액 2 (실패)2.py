import sys

sys.stdin = open("그리디-만들 수 없는 금액.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nl = sorted(list(map(int, input().split())))
    print(nl)

    target = 1
    for x in nl:
        print(target,x)
        if target < x:
            break
        target += x

    print(target)