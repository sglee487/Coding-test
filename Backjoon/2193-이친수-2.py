import sys
import math
sys.setrecursionlimit(10**9)

sys.stdin = open("2193-이친수.txt", "r")

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
    exit()
if N == 2:
    print(1)
    exit()

a, b = 1, 1
result = 0
for _ in range(N-2):
    result = a + b
    a = b
    b = result
print(result)