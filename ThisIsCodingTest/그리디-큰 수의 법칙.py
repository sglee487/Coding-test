import sys

sys.stdin = open("그리디-큰 수의 법칙.txt", "r")

n, m, k = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()
now_k = k
result = 0
for _ in range(m):
    if now_k > 0:
        result += nlist[-1]
        now_k -= 1
    else:
        result += nlist[-2]
        now_k = k
print(result)