import sys

sys.stdin = open("그리디-만들 수 없는 금액.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nl = list(map(int, input().split()))
    nl.sort()
    print(nl)
    now_index = 0
    for i in range(N):
        if sum(nl[:i])+1 < nl[i]:
            break
        else:
            now_index = i+1
    print(sum(nl[:now_index])+1)