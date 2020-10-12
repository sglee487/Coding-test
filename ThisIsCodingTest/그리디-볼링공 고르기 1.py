import sys

sys.stdin = open("그리디-볼링공 고르기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    boring = list(map(int, input().split()))

    result = 0
    oneball = int()
    for i in range(len(boring)):
        oneball = boring[i]
        for j in range(i+1,len(boring)):
            if boring[j] != oneball:
                result += 1

    print(result)
