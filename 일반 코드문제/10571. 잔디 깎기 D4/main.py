import sys

sys.stdin = open("input2.txt", "r")

def is_safe(now_r,now_c):
    now_e = H[now_r][now_c]

    for r in range(N):
        if H[r][now_c] > now_e: return False

    return True

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())

    H = [[0] * N for _ in range(M)]
    for i in range(N):
        H[i] = list(map(int, input().split()))

    print(H)

    HR = [0 for _ in range(N)]
    for i,c in enumerate(zip(*H)):
        HR[i] = list(c)

    result = True
    for r in range(N):
        pre_c = 0
        for c in range(1, N):
            print(r,c)
            if H[r][pre_c] != H[r][c]:
                print(is_safe(r,c))
                if not(is_safe(r,c)):
                    result = False
                    break
            pre_c = c
        if not(result): break
    print(result)
    print("#{}".format(test_case))
    # ///////////////////////////////////////////////////////////////////////////////////
