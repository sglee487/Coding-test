# https://programmers.co.kr/learn/courses/30/lessons/60060
from collections import defaultdict

def find_lindex(words,q):
    lenq = len(q)
    inq = q.index('?')
    l, r = 0, len(words)-1
    result = -1
    while l<=r:
        mid = (l+r) // 2
        if len(words[mid]) > lenq:
            r = mid-1
        elif len(words[mid]) < lenq:
            l = mid+1
        else:
            if words[mid][:inq] > q[:inq]:
                r = mid-1
            elif words[mid][:inq] < q[:inq]:
                l = mid+1
            else:
                result = mid
                r = mid-1
    return result

def find_rindex(words,q):
    lenq = len(q)
    inq = q.index('?')
    l, r = 0, len(words)-1
    result = -1
    while l<=r:
        mid = (l+r) // 2
        if len(words[mid]) > lenq:
            r = mid-1
        elif len(words[mid]) < lenq:
            l = mid+1
        else:
            if words[mid][:inq] > q[:inq]:
                r = mid-1
            elif words[mid][:inq] < q[:inq]:
                l = mid+1
            else:
                result = mid
                l = mid+1
    return result

def solution(words, queries):
    qid = defaultdict(int)
    for i, q in enumerate(queries):
        qid[q] = i
    # print(words)
    # print(queries)
    answer = [0] * len(queries)
    qsw = []
    qew = []
    for q in queries:
        if q[0] != '?':
            qsw.append(q)
        else:
            qew.append(q)
    wordsreverse = [w[::-1] for w in words]
    qewr = [w[::-1] for w in qew]
    swords = sorted(words,key= lambda x:[len(x),x])
    # print(swords)
    # print(sorted(qsw,key= lambda x:[len(x),x]))
    swordsreverse = sorted(wordsreverse,key= lambda x:[len(x),x])
    # print(swordsreverse)
    # print(sorted(qewr,key= lambda x:[len(x),x]))
    for q in sorted(qsw,key= lambda x:[len(x),x]):
        lindex = find_lindex(swords,q)
        rindex = find_rindex(swords,q)
        # print(q,lindex,rindex)
        if lindex == -1 and rindex == -1: continue
        answer[qid[q]] = rindex - lindex + 1
    for q in sorted(qewr,key= lambda x:[len(x),x]):
        lindex = find_lindex(swordsreverse,q)
        rindex = find_rindex(swordsreverse,q)
        # print(q,lindex,rindex)
        if lindex == -1 and rindex == -1: continue
        answer[qid[q[::-1]]] = rindex - lindex + 1
    # print(qid)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]),[3, 2, 4, 1, 0])
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?","?????","ab?","??????","????"]),[3, 2, 4, 1, 0, 5, 0,1,0])
print(solution(["abcde","abcdf","abcdg"],["abcd?","abc??","ab???","ab??","??cde","???dg"]),[3,3,3,0,1,1])
print(solution(["gggba","gggab","ggefe","ggff"],["???ba","???ab","?????","gg???","???f"]),[1,1,3,3,1])
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["????o", "fr???", "fro???", "pro?", "fro??"]),[2, 4, 1, 0, 3])