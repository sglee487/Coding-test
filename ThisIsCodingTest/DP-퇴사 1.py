import sys

sys.stdin = open("DP-퇴사.txt", "r",encoding='utf-8')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    T = [0] * N
    P = [0] * N
    for i in range(N):
        T[i], P[i] = map(int, input().split())
    # print(T)
    # print(P)
    earn = [0] * N
    for i in range(N):
        if i + T[i] <= N:
            earn[i] += P[i]
        for j in range(i + T[i],N):
            earn[j] = max(earn[j],earn[i])
        # print(earn)
    # print(earn)
    # print()
    print(max(earn))