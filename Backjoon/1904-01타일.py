import sys
import math
sys.setrecursionlimit(10**9)

sys.stdin = open("1904-01타일.txt", "r")

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
    exit()
if N == 2:
    print(2)
    exit()

da = 1
db = 2
dc = int()

for i in range(3, N+1):
    dc = (da + db) % 15746
    da = db
    db = dc

print(dc)
