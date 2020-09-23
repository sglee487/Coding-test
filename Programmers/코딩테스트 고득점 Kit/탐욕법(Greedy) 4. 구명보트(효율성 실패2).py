def solution(people, limit):
    answer = 0
    boat = []
    while people:
        boat.append(people[0])
        rest = limit - boat[0]
        g = set(range(40,rest+1)) & set(people[1:])
        if g:
            boat.append(max(g))
        for b in boat:
            people.remove(b)
        boat = []
        answer += 1
    return answer

print(solution([50, 50],100),1)
print(solution([70, 50, 80, 50],100),3)
print(solution([70, 50, 80],100),3)