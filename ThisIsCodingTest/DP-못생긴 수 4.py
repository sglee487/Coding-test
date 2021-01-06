import sys

sys.stdin = open("DP-못생긴 수.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    a = 2
    b = 3
    c = 5
    agly = [1]
    while True:
        if len(agly) >= n: break
        ag = min(a,b,c)
        agly.append(ag)
        if ag == a:
            a += 2
        if ag == b:
            b += 3
        if ag == c:
            c += 5
    print(agly)
    print(agly[n-1])