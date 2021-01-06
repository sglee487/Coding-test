import sys

sys.stdin = open("그리디-큰 수의 법칙.txt", "r")

n, m, k = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()

tulen = k+1
tusum = (nlist[-1]*k) + nlist[-2]
