import sys

sys.stdin = open("DP-편집 거리.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    A = list(input())
    B = list(input())
    print(A,B)