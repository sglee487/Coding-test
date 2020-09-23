def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

print(solution([50, 50],100),1)
print(solution([20, 30, 50, 60, 70, 80, 90],100),5)
print(solution([70, 50, 80, 50],100),3)
print(solution([70, 50, 80],100),3)

from collections import deque

def solution(people, limit):
    answer = 0
    poo = deque(sorted(people))
    while poo:
        if len(poo) == 1:
            answer += 1
            break
        if poo[0] + poo[-1] > limit:
            poo.pop()
            answer += 1
        else:
            poo.popleft()
            poo.pop()
            answer += 1
    return answer

print(solution([50, 50],100),1)
print(solution([20, 30, 50, 60, 70, 80, 90],100),5)
print(solution([70, 50, 80, 50],100),3)
print(solution([70, 50, 80],100),3)