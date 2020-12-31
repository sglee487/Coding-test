import math

def solution(n,m):
    N = n
    blocks = 1
    cutcount = 0
    while True:
        n = n // 2
        blocks *= 2
        cutcount += int((blocks / m))
        if blocks >= N: break
    return cutcount

print(solution(8,3),4)
print(solution(20,3))
print(solution(100,5))