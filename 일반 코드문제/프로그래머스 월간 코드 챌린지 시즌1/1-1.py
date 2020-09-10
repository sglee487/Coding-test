from itertools import combinations

def solution(numbers):
    answer = []
    # answerset = set()
    # bs = combinations(numbers,2)
    # print(list(bs))
    # for a, b in bs:
    #     print(a,b)
    #     answerset.add(a+b)
    # print(answerset)

    answerset = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answerset.add(numbers[i]+numbers[j])

    answer = sorted(list(answerset))

    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))