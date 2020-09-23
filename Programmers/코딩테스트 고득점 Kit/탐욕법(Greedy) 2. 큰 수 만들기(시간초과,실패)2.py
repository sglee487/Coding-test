def solution(number, k):
    answer = number[:]
    canswer = answer[:]
    for ck in range(k):
        for i in range(len(answer)):
            if answer[:i] + answer[i+1:] > canswer:
                canswer = answer[:i] + answer[i+1:]
        answer = canswer
    return answer

print(solution("1924",2),"94")
print(solution("1231234",3),"3234")
print(solution("4177252841",4),"775841")