import sys
import math
sys.setrecursionlimit(10**9)

sys.stdin = open("2981-검문-2.txt", "r")

# input = sys.stdin.readline

def gcd(m, n):
    while n != 0:
        t = m % n
        m, n = n, t
    return abs(m)

N = int(input())
ml = []
for _ in range(N):
    ml.append(int(input()))

dl = [ml[i+1] - ml[i] for i in range(len(ml)-1)]
dl.sort()
M = int()
for de in dl:
    M = gcd(M, de)

yac = set()
for i in range(1, math.ceil(math.sqrt(M))+1):
    if M % i == 0:
        yac.add(i)
        yac.add(M // i)
yac.remove(1)

print(*sorted(list(yac)))