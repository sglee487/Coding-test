### code from : junhwanyun

import sys

sys.stdin = open("s_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    PNL = [True] * 1000
    for i in range(2,32):
        if PNL[i]:
            for j in range(i*i,1000,i):
                PNL[j] = False

    goal = int(input())
    result = 0

    for x in range(2,1000):
        if x * 3 > goal: break
        if (PNL[x]):
            for y in range(x,1000):
                if x + y * 2 > goal: break
                if PNL[y]:
                    z = goal - x - y
                    if z < y: break
                    if PNL[z]: result += 1

    print("#{}".format(test_case), result)
    # ///////////////////////////////////////////////////////////////////////////////////
