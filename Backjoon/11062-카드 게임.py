import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("11062-카드 게임-1.txt", "r")

input = sys.stdin.readline

def dfs(cards, s, e, total):
    if dp[s][e]:
        return dp[s][e]
    if s == e:
        dp[s][e] = cards[s]
        return dp[s][e]
    dp[s][e] = max(total - dfs(cards, s,e-1, total-cards[e]), total - dfs(cards, s+1,e, total-cards[s]))
    return dp[s][e]

T = int(input())
for test_case in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    if N == 1:
        print(cards[0])
        continue
    dp = [[0] * N for _ in range(N)]
    answer = dfs(cards,0,N-1, sum(cards))
    print(answer)