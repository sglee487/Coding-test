import sys

sys.stdin = open("DP-못생긴 수.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    aglynum = [1,2,3,4,5]
    num = 6
    while len(aglynum) < n:
        for onem in aglynum[1:]:
            for twom in aglynum[2:]:
                if num == onem * twom:
                    aglynum.append(num)
                    break
            if aglynum[-1] == num: break
        print(len(aglynum),aglynum)
        num += 1
    print(aglynum[n-1])