from itertools import combinations
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("1039-교환-8.txt", "r")

input = sys.stdin.readline

N, K = map(int, input().split())
M = len(str(N))

N = str(N)

if M == 1:
    print(-1)
    exit()
if M <= 2 and N[1] == '0':
    print(-1)
    exit()

one_total = [N]
for _ in range(K):
    temp_total = set()
    for n in one_total:
        for i, j in combinations(range(M),2):
            nl = list(n)
            nl[i], nl[j] = nl[j], nl[i]
            if nl[0] == '0': continue
            temp_total.add(tuple(nl))

    temp_total = sorted(list(temp_total))
    one_total = temp_total.copy()

print(''.join(one_total[-1]))
