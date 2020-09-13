def solution(n):
    new_n = str(n)
    pluscount = 0
    while eval(new_n) >= 10:
        si = len(new_n) // 2
        while True:
            n1, n2 = new_n[:si] , new_n[si:]
            if n2[0] == '0' and len(n2) != 1:
                si += 1
            else: break
        hap = eval(n1) + eval(n2)
        pluscount += 1
        new_n = str(hap)

    return [pluscount, int(new_n)]

print(solution(73425))
print(solution(10007))
print(solution(9))