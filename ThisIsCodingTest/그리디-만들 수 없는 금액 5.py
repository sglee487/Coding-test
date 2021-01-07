import sys

sys.stdin = open("그리디-만들 수 없는 금액.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nlist = list(map(int, input().split()))
    nlist.sort()
    print(nlist)
    target = 1
    for num in nlist:
        if num > target:
            break
        else:
            target += num
    print(target)