def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        print(i, citations[i], citations, l-i)
        if citations[i] >= l-i:
            return l-i
    return 0
print(solution([3, 0, 6, 1, 5]),3)
print(solution([1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]),7)
print(solution([0, 1, 3, 5, 5, 5, 5, 5, 5, 6]),5)
print(solution([22, 42]),2)
print(solution([20,19,18,1]),3)
def solution(citations):
    citations.sort(reverse=True)
    print(list(enumerate(citations, start=1)))
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
print(solution([3, 0, 6, 1, 5]),3)
print(solution([1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]),7)
print(solution([0, 1, 3, 5, 5, 5, 5, 5, 5, 6]),5)
print(solution([22, 42]),2)
print(solution([20,19,18,1]),3)