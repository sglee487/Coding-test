def solution(name):
    N = len(name)
    result = 0
    nl = list(name)
    i = 0
    while not all(n == 'A' for n in nl):
        ld, rd = 0, 0
        while nl[i-ld] == 'A': ld += 1
        while nl[(i+rd)%N] == 'A': rd += 1
        if ld < rd:
            i = i-ld
            result += ld
        else:
            i = (i+rd)%N
            result += rd
        result += min(abs(ord("A") - ord(nl[i])),abs(ord("[") - ord(nl[i])))
        nl[i] = 'A' 
    # for n in name:
    #     result += min(abs(ord("A") - ord(n)),abs(ord("[") - ord(n)))
    # print(result)

    return result

print(solution("JEROEN"),56)
print(solution("JAN"),23)
print(solution("AAAAAAA"),23)
print(solution("ECAAAAADA"))
print(solution("CACACAAAAAAAAACA"))
print(solution("CACACAAAAAAAACAA"))