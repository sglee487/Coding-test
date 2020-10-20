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
    dp = [0] * (N+1)
    max_value = 0
    for i in range(N - 1, -1, -1):
        time = T[i] + i
        # 상담이 기간 안에 끝나는 경우
        if time <= N:
            # 점화식에 맞게, 현재까지의 최고 이익 계산
            dp[i] = max(P[i] + dp[time], max_value)
            max_value = dp[i]
        # 상담이 기간을 벗어나는 경우
        else:
            dp[i] = max_value
        print(dp)
    print(dp)
    print(max_value)