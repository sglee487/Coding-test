from itertools import combinations

def solution(number, k):
    return str(max(map(int,map(''.join,combinations(number,len(number)-(k))))))

print(solution("1924",2),"94")
print(solution("1231234",3),"3234")
print(solution("4177252841",4),"775841")