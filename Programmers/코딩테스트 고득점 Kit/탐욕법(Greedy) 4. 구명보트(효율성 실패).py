def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    boat = []
    while people:
        for p in people:
            if limit - sum(boat) >= p:
                boat.append(p)
            if len(boat) == 2: break
        for b in boat:
            people.remove(b)
        answer += 1
        boat = []
    return answer

print(solution([70, 50, 80, 50],100),3)
print(solution([70, 50, 80],100),3)