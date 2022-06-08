import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("CANADATRIP-1.txt", "r")

input = sys.stdin.readline



def isOver(distance, N, K, L, M, G):
    signIndex = 0
    for i in range(N):
        if distance >= L[i]-M[i]:
            signIndex += ((min(L[i], distance)-(L[i]-M[i])) // G[i])+1
    return signIndex >= K

def solve(N,K,L,M,G):

    lo, hi = -1, 8030001
    while lo+1<hi:
        mid = (lo + hi) // 2
        if isOver(mid, N, K, L, M, G):
            hi = mid
        else:
            lo = mid
    return hi


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    L, M, G = [], [], []
    for _ in range(N):
        tempInput = list(map(int, input().split()))
        L.append(tempInput[0])
        M.append(tempInput[1])
        G.append(tempInput[2])
    print(solve(N,K,L,M,G))