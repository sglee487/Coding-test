# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    stages.sort()
    # print(stages)
    lens = len(stages)
    result = []
    for i in range(1,N+1):
        if lens == 0:
            result.append((0,i))
        else:
            result.append((stages.count(i)/lens,i))
            lens -= stages.count(i)
    result.sort(key=lambda x:-x[0])
    # print(result)
    result = [e[1] for e in result]
    return result

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]),[3,4,2,1,5])
print(solution(4,[4,4,4,4,4]),[4,1,2,3])