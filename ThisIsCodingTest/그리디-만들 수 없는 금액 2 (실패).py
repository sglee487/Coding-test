import sys

sys.stdin = open("그리디-만들 수 없는 금액.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nl = sorted(list(map(int, input().split())))
    print(nl)
    dp = [False] * (sum(nl)+1)
    stack = [0]
    sri = 0
    li = 0
    for i in range(len(dp)):
        print(i)
        if sum(stack) >= i:
            dp[i] = True
        else:
            if sum(stack) + nl[sri] == i:
                stack.append(nl[sri])
                sri += 1
                dp[i] = True
            else:
                li = i
                break
    print(li)
    print(dp)