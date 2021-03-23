import sys

sys.stdin = open("2579-계단 오르기-1.txt", "r")

input = sys.stdin.readline

N = int(input())
stairs = [0] * (301)
for i in range(1,N+1):
    stairs[i] = int(input())

dp = [0]
dp.append(stairs[1])
dp.append(stairs[1]+stairs[2])
dp.append(max(stairs[1]+stairs[3],
              stairs[2]+stairs[3]))

for i in range(4,N+1):
    dp.append(max(dp[i-2]+stairs[i],
                  dp[i-3]+stairs[i-1]+stairs[i]))

print(dp[N])