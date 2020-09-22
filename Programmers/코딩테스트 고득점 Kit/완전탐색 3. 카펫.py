def solution(brown, yellow):
    totalg = brown + yellow
    canl = []
    answer = [0,0]
    for i in range(totalg,0,-1):
        if totalg//i > i: break
        if totalg % i == 0:
            if (i-2) * ((totalg//i) - 2) == yellow:
                answer[0], answer[1] = i, totalg//i
                break
            canl.append((i,totalg//i))
    print(canl)
    return answer

print(solution(10,2),[4,3])
print(solution(8,1),[3,3])
print(solution(24,24),[8,6])