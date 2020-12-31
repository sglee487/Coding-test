def cutbar(n,m,cutcurrent):
    if cutcurrent >= n:
        return 0
    if cutcurrent <= m:
        return 1+cutbar(n,m,cutcurrent + cutcurrent)
    else:
        return 1+cutbar(n,m,cutcurrent + m)


def solution(n,m):

    return cutbar(n,m,1)

print(solution(8,3),4)
print(solution(20,3),8)
print(solution(100,5),22)