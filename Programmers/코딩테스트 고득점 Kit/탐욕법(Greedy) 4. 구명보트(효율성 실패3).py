def solution(people, limit):
    answer = 0
    boat = [0,0]
    while sum(people) != 0:
        boat[0] = max(people)
        people[people.index(boat[0])] = 0
        rest = limit - boat[0]
        g = set(range(40,rest+1)) & set(people)
        if g:
            boat[1] = (max(g))
            people[people.index(boat[1])] = 0
        boat = [0,0]
        answer += 1
    return answer

print(solution([50, 50],100),1)
print(solution([70, 50, 80, 50],100),3)
print(solution([70, 50, 80],100),3)