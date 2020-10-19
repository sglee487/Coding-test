import sys

sys.stdin = open("DP-개미 전사.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))

    d = [0] * 100

    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, N):
        d[i] = max(d[i-1], d[i-2] + array[i])

    print(d[N-1])