# https://programmers.co.kr/learn/courses/30/lessons/60060
# https://github.com/ndb796/python-for-coding-test/blob/master/15/4.py
from bisect import bisect_left,bisect_right
def count_range(words,lq,rq):
    li = bisect_left(words,lq)
    ri = bisect_right(words,rq)
    return ri-li

def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    arrayr = [[] for _ in range(10001)]
    for w in words:
        array[len(w)].append(w)
        arrayr[len(w)].append(w[::-1])

    for i in range(10001):
        array[i].sort()
        arrayr[i].sort()

    for q in queries:
        if q[0] != '?':
            answer.append(count_range(array[len(q)],q.replace('?','a'),q.replace('?','z')))
        else:
            answer.append(count_range(arrayr[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z')))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]),[3, 2, 4, 1, 0])
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?","?????","ab?","??????","????"]),[3, 2, 4, 1, 0, 5, 0,1,0])
print(solution(["abcde","abcdf","abcdg"],["abcd?","abc??","ab???","ab??","??cde","???dg"]),[3,3,3,0,1,1])
print(solution(["gggba","gggab","ggefe","ggff"],["???ba","???ab","?????","gg???","???f"]),[1,1,3,3,1])
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["????o", "fr???", "fro???", "pro?", "fro??"]),[2, 4, 1, 0, 3])