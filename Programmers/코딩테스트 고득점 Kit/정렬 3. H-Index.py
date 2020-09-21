def solution(citations):
    scl = sorted(citations)
    # print(scl)
    # ant = list()
    answer = 0
    for n in range(len(scl)+1):
        count = 0
        for c in scl:
            if c >= n:
                count += 1
        if n > count: break
        answer = n
        # ant.append((n,count))
    return answer

print(solution([3, 0, 6, 1, 5]),3)
print(solution([1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]),7)
print(solution([0, 1, 3, 5, 5, 5, 5, 5, 5, 6]),5)
print(solution([22, 42]),2)
print(solution([20,19,18,1]),3)