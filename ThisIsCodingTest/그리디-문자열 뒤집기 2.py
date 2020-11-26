import sys

sys.stdin = open("그리디-문자열 뒤집기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    S = list(map(int,input()))
    dp = [0] * (len(S)-1)
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            dp[i] = 0
        else:
            dp[i] = 1
    # print(S)
    # print(dp)
    print((sum(dp)+1)//2)