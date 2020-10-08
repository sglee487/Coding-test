def solution(n):
    def to_jin(num, divnum):
        q, r = divmod(num,divnum)
        return to_jin(q,divnum) + str(r) if q!=0 else str(r)
    to3jin = to_jin(n,3)
    def to_10_jin(num, orijin):
        ttn = 0
        for i, n in enumerate(str(num)):
            ttn += int(n)*(orijin ** i)
        return ttn
    return to_10_jin(to_jin(int(''.join(to3jin)),10),3)

print(solution(45),7)
print(solution(125),229)