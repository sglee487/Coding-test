import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("14718-용감한 용사 진수-2.txt", "r")

input = sys.stdin.readline

N, K = map(int, input().split())
soldiers = list(list(map(int, input().split())) for _ in range(N))

# print(N,K)
# print(soldiers)

result = 10e9

for i in range(N):
    for j in range(N):
        for k in range(N):
            a = soldiers[i][0]
            b = soldiers[j][1]
            c = soldiers[k][2]
            win = 0

            for l in range(N):
                if a >= soldiers[l][0] and b >= soldiers[l][1] and c >= soldiers[l][2]:
                    win += 1
                if win >= K:
                    result = min(result, a+b+c)

print(result)