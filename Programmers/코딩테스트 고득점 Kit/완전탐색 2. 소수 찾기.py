from itertools import permutations

def solution(numbers):
    pns = set()
    print(list(permutations(numbers,1)))
    for i in range(1,len(numbers)+1):
        for e in permutations(numbers,i):
            print(''.join(e),int(''.join(e)))
            pns.add(int(''.join(e)))
    print(pns)
    result = 0
    for n in list(pns):
        if n <= 1: continue
        prime = True
        for i in range(2,n//2+1):
            if n % i == 0:
                prime = False
                break
        if prime: result += 1
    print(result)
    return result

print(solution("17"),3)
print(solution("011"),2)