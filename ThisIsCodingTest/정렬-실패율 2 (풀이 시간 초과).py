from collections import defaultdict

# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    stages.sort()
    stagesreverse = stages[::-1]
    failreatesdict = defaultdict(int)
    pn = list(set(stages))
    for i in range(1,N+1):
        failreatesdict[i] = 0
    for i in pn:
        liindex = stages.index(i)
        riindex = len(stages) - stagesreverse.index(i)
        failreatesdict[i] = (riindex-liindex) / (len(stages)-liindex)
    if N+1 in failreatesdict: del failreatesdict[N+1]
    faillist = list(failreatesdict.items())
    faillist.sort(key=lambda x:-x[1])
    result = [e[0] for e in faillist]

    return result

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]),[3,4,2,1,5])
print(solution(4,[4,4,4,4,4]),[4,1,2,3])