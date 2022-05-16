import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("SUSHI-1.txt", "r")

input = sys.stdin.readline


C = int(input())
for _ in range(C):
    n, m = map(int, input().split())
    m //= 100
    pl, wl = [], []
    for _ in range(n):
        p, w = map(int, input().split())
        pl.append(p//100)
        wl.append(w)

    weightMax = 0
    cache = [0] * 201
    for budget in range(1, m+1):
        cache[budget%201] = 0
        for item in range(n):
            if budget < pl[item]: continue
            cache[budget%201] = max(cache[budget%201],
                                    cache[(budget-pl[item])%201] + wl[item])
        weightMax = max(weightMax, cache[budget%201])
    print(weightMax)