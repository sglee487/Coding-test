import sys

sys.stdin = open("DP-효율적인 화폐 구성.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    array=[]
    for i in range(n):
        array.append(int(input()))

    d = [10001] * (m+1)

    d[0] = 0
    for i in range(n):
        for j in range(array[i], m+1):
            d[j] = min(d[j], d[j - array[i]] + 1)

    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])