import sys

sys.stdin = open("DP-개미 전사.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    fl = list(map(int, input().split()))
    print(fl)
    tfl1 = [0] * N
    tfl2 = [0] * N
    tfl1[0] = 1
    tfl2[1] = 3
    for i in range(2,len(fl)):
        tfl1[i] = max(tfl1[i-1], tfl1[i-2] + fl[i])
        tfl2[i] = max(tfl2[i-1], tfl2[i-2] + fl[i])
    print(tfl1)
    print(tfl2)
    print(max(tfl1[-1],tfl2[-1]))