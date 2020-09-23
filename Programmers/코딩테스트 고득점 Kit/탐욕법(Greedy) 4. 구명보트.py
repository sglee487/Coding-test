def solution(people, limit):
    people.sort()
    spare = 0
    i, j = 0, len(people)-1
    while i < j:
        rest = limit - people[i]
        while rest < people[j]:
            j -= 1
            if i == j:break
        if i == j: break
        spare += 1
        i += 1
        j -= 1
    return len(people) - spare

print(solution([50, 50],100),1)
print(solution([20, 30, 50, 60, 70, 80, 90],100),5)
print(solution([70, 50, 80, 50],100),3)
print(solution([70, 50, 80],100),3)