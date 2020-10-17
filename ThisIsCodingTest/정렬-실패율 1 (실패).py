# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    stages.sort()
    lr = []
    for e in range(1,N+1):
        i = stages.find(e)
        if i == -1:
            lr.append((0, e))
        else:
            lr.append((stages.count(e) / len(stages[i:]),e))
    print(sorted(lr,key=lambda x:x[0]))
    answer = []
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]),[3,4,2,1,5])
print(solution(4,[4,4,4,4,4]),[4,1,2,3])