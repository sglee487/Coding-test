def solution(answers):
    onestu = [1,2,3,4,5]
    twostu = [2,1,2,3,2,4,2,5]
    threestu = [3,3,1,1,2,2,4,4,5,5]
    stuscore = [0 for _ in range(3)]
    for i in range(len(answers)):
        if onestu[i%len(onestu)] == answers[i]: stuscore[0] = stuscore[0] + 1
        if twostu[i%len(twostu)] == answers[i]: stuscore[1] = stuscore[1] + 1
        if threestu[i%len(threestu)] == answers[i]: stuscore[2] = stuscore[2] + 1
    maxscore = max(stuscore)
    answer = []
    for i in range(3):
        if stuscore[i] == maxscore:
            answer.append(i+1)
    return answer

print(solution([1,2,3,4,5]),[1])
print(solution([1,3,2,4,2]),[1,2,3])