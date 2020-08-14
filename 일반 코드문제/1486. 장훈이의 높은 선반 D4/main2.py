import sys

sys.stdin = open("input.txt", "r")

# 173 ms
def solve(N,B,allsum):
    lowest_H = 200000
    stack = []

    stack.append((N-1,0,allsum))
    while stack:
        i, S, R = stack.pop()
        if S >= B:
            lowest_H = min(lowest_H,S)
        if R < B: continue
        if i >= 0:
            stack.append((i - 1, S + H[i], R))
            stack.append((i - 1, S, R - H[i]))

    return lowest_H

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    allsum = sum(H)

    # 173 ms
    lowest_H = solve(N,B,allsum)

    print("#{}".format(test_case), lowest_H - B)
    # ///////////////////////////////////////////////////////////////////////////////////
