# https://programmers.co.kr/learn/courses/30/lessons/60060
from collections import defaultdict
from bisect import bisect_left,bisect_right

def solution(words, queries):
    maxwordlen = 0
    for w in words:
        maxwordlen = max(maxwordlen,len(w))
    maxquerlen = 0
    for q in queries:
        maxquerlen = max(maxquerlen, len(q))
    maxlen = max(maxwordlen,maxquerlen)
    qdict = defaultdict(int)
    qi = []
    for i,q in enumerate(queries):
        qdict[q] = 0
        qi.append((i,q))
    words.sort()
    rwords = [s[::-1] for s in words]
    rwords.sort()
    wordsslen = [[] for _ in range(maxlen+1)]
    for w in words:
        wordsslen[len(w)].append(w)
    rwordsslen = [[] for _ in range(maxlen+1)]
    for rw in rwords:
        rwordsslen[len(rw)].append(rw)
    ssqueries = [e for e in queries if e[-1] == '?' ]
    resqueries = [e[::-1] for e in queries if e[0] == '?']
    ssqueries.sort()
    resqueries.sort()
    ssqueriesslen = [[] for _ in range(maxlen+1)]
    resqueriesslen = [[] for _ in range(maxlen+1)]
    for sq in ssqueries:
        ssqueriesslen[len(sq)].append(sq)
    for req in resqueries:
        resqueriesslen[len(req)].append(req)
    for l in range(maxlen+1):
        if not ssqueriesslen[l]: continue
        for q in ssqueriesslen[l]:
            count = (bisect_right(wordsslen[l],q.replace('?','z')) - bisect_left(wordsslen[l],q.replace('?','a')))
            qdict[q] = count
    for l in range(maxlen+1):
        if not resqueriesslen[l]: continue
        for q in resqueriesslen[l]:
            count = (bisect_right(rwordsslen[l],q.replace('?','z')) - bisect_left(rwordsslen[l],q.replace('?','a')))
            qdict[q[::-1]] = count
    # print(qdict)
    answer = [0] * len(queries)
    for i, q in qi:
        answer[i] = qdict[q]
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]),[3, 2, 4, 1, 0])
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?","?????","ab?","??????","????"]),[3, 2, 4, 1, 0, 5, 0,1,0])
print(solution(["abcde","abcdf","abcdg"],["abcd?","abc??","ab???","ab??","??cde","???dg"]),[3,3,3,0,1,1])
print(solution(["gggba","gggab","ggefe","ggff"],["???ba","???ab","?????","gg???","???f"]),[1,1,3,3,1])
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["????o", "fr???", "fro???", "pro?", "fro??"]),[2, 4, 1, 0, 3])