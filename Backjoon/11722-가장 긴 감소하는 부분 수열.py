import sys
from bisect import bisect_left

sys.stdin = open("11722-가장 긴 감소하는 부분 수열-1.txt", "r")

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
AR = A[::-1]
# print(AR)
LIS = [1]
C = [0] + [1001] * (N+1)
c_index = 0
for a in AR:
    c_index = bisect_left(C,a)
    C[c_index] = a
    LIS.append(c_index)

LIS = [e for e in LIS if e <= 1000]
print(max(LIS))