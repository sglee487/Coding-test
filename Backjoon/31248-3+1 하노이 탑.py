import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("31248-3+1 하노이 탑-2.txt", "r")

# N = int(sys.stdin.readline().strip())
N = 5

def hanoi(n, src, mid, dst):
    if n == 0:
        return
    hanoi(n - 1, src, dst, mid)
    print(src, dst)
    hanoi(n - 1, mid, src, dst)


dp = [0] * (N+1)
dp[1] = 1
for i in range(2, N+1):
    dp[i] = (2 ** (i-2) - 1) + 3 + dp[i-2]

print(dp[N])

current = 'A'

while N >= 2:

    mid_dst = 'C' if current == "A" else 'A'

    hanoi(N - 2, current, 'B', mid_dst)

    print(current, 'B')
    print(current, 'D')
    print('B', 'D')

    N -= 2
    current = mid_dst

if N == 1:
    print(current, 'D')