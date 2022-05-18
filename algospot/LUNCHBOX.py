import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("LUNCHBOX-1.txt", "r")

input = sys.stdin.readline


C = int(input())
for _ in range(C):
    n = int(input())
    ml = list(map(int, input().split()))
    el = list(map(int, input().split()))
    eil = [(e,i) for e, i in zip(el, range(n))]
    eil.sort(key=lambda x:(-x[0]))
    M = sum(ml)
    totalTime = 0
    beginEat = 0
    for e,i in eil:
        beginEat += ml[i]
        totalTime = max(totalTime, beginEat + e)
    print(totalTime)