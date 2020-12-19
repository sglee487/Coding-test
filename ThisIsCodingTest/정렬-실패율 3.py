from bisect import bisect_left,bisect_right

# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    stages.sort()
    slen = len(stages)
    failrate = [0] * (N+1)
    for stage in range(1,N+1):
        li = bisect_left(stages,stage)
        ri = bisect_right(stages,stage)
        if (slen-li) == 0: continue
        failrate[stage] = (ri - li) / (slen-li)
    failtu = []
    for i in range(1,N+1):
        failtu.append((failrate[i],i))
    failtu.sort(key=lambda x:-x[0])
    result = [e[1] for e in failtu]
    return result

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]),[3,4,2,1,5])
print(solution(4,[4,4,4,4,4]),[4,1,2,3])