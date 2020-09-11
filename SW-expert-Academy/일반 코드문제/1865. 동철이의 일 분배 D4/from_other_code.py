import sys

sys.stdin = open("input2.txt", "r")


for t in range(int(input())):
    # this code is from https://swexpertacademy.com/main/userpage/home/userHome.do?userId=AWllraL6jfYDFASP
    n = int(input())
    p = [[*map(lambda x: x / 100, map(int, input().split()))] for _ in range(n)]

    # print(p)
    # print(1 << n)

    d = [0] * (1 << n)
    d[0] = 1
    for mask in range(1 << n):
        x = sum(1 for i in range(n) if mask & (1 << i))
        for j in range(n):
            if mask & (1 << j) == 0:
                d[mask | (1 << j)] = max(d[mask | (1 << j)], d[mask] * p[x][j])
                # print("mask:",mask, ", (1 << j):",(1 << j), ", mask | (1 << j):", mask | (1 << j), d)
    # print(d)
    print(f'#{t + 1} {d[-1] * 100:.6f}')