import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("GENIUS-1.txt", "r")

input = sys.stdin.readline


def solve(N,K,M,LI,T,QI):
    cache = [[0.] * (N+1) for _ in range(5)]
    cache[0][0] = 1.0
    for time in range(1, K+1):
        for nowSong in range(N):
            percent = 0.
            for prevSong in range(N):
                percent += (cache[(time-LI[prevSong]) % 5][prevSong]*T[prevSong][nowSong])
            cache[time % 5][nowSong] = percent
    answer = []
    for song in QI:
        prob = 0.
        for time in range(K-LI[song]+1,K+1):
            prob += cache[time%5][song]
        answer.append(prob)
    return answer


C = int(input())
for _ in range(C):
    N, K, M = map(int, input().split())
    LI = list(map(int, input().split()))
    T = [list(map(float, input().split())) for _ in range(N)]
    QI = list(map(int, input().split()))
    answerList = solve(N,K,M,LI,T,QI)
    print(answerList)