import sys

sys.stdin = open("DP-효율적인 화폐 구성.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    money = [10001] * (10001)
    for _ in range(N):
        money[int(input())] = 1
    for i in range(1,M+1):
        for a in range(1,i):
            money[i] = min(money[i],money[a] + money[i-a])
    print(money)
    print(money[M] if money[M] != 10001 else -1)