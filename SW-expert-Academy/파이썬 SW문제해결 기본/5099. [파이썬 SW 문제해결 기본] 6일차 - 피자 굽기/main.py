
import sys

sys.stdin = open("sample_input.txt", "r")

def f1(x):
    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    TC = [[i+1,c] for i,c in enumerate(C)]

    wha = []
    for i in range(N):
        wha.append(TC.pop(0))

    t = 0
    pn = 0
    while True:
        wha[t%N][1] = wha[t%N][1] // 2
        if wha[t%N][1] == 0:
            pn = wha[t%N][0]
            if TC:
                wha[t % N] = TC.pop(0)
        t += 1
        if sum(p[1] for p in wha) == 0: break

    print("#{}".format(test_case),pn)

    # ///////////////////////////////////////////////////////////////////////////////////
