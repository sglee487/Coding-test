def solution(number, k):
    answer = number[:]
    previ = 0
    for _ in range(k):
        shouldcuti = len(answer)-1
        for i in range(previ, len(answer)-1):
            if answer[i+1] > answer[i]:
                shouldcuti = i
                break
        answer = answer[:shouldcuti] + answer[shouldcuti + 1:]
        previ = shouldcuti - 1 if shouldcuti - 1 >= 0 else 0
        print(answer, previ)
    return answer

print(solution("1924",2),"94")
print(solution("1231234",3),"3234")
print(solution("4177252841",4),"775841")
print(solution("54321",2),"543")
print(solution("54123",1),"5423")
print(solution("54123",2),"543")