import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11726-2xn 타일링-2-2.txt", "r")

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
    dc = (da + db) % 10007
    da = db
    db = dc
print(dc)