import sys

sys.stdin = open("DP-못생긴 수.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    if n == 1: print(1)
    count = 1
    two = 2
    three = 3
    five = 5
    num = 1
    ag = [1]
    while count < n:
        num += 1
        if num % 2 == 0:
            count += 1
            ag.append(num)
        elif num % 3 == 0:
            count += 1
            ag.append(num)
        elif num % 5 == 0:
            count += 1
            ag.append(num)
        print(num,count)
    print(ag)
    print(count)
    print(num)