# https://programmers.co.kr/learn/courses/30/lessons/60060
from bisect import bisect_left,bisect_right

# https://github.com/ndb796/python-for-coding-test/blob/master/15/4.py
def solution(words, queries):
    answer = []
    wordsslen = [[] for _ in range(10001)]
    rwordsslen = [[] for _ in range(10001)]
    for w in words:
        wordsslen[len(w)].append(w)
        rwordsslen[len(w)].append(w[::-1])
    for i in range(10001):
        wordsslen[i].sort()
        rwordsslen[i].sort()

    for q in queries:
        if q[-1] == '?':
            count = (bisect_right(wordsslen[len(q)],q.replace('?','z'))-bisect_left(wordsslen[len(q)],q.replace('?','a')))
        elif q[0] == '?':
            count = (bisect_right(rwordsslen[len(q)], q[::-1].replace('?', 'z')) - bisect_left(rwordsslen[len(q)],q[::-1].replace('?', 'a')))
        answer.append(count)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]),[3, 2, 4, 1, 0])
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?","?????","ab?","??????","????"]),[3, 2, 4, 1, 0, 5, 0,1,0])
print(solution(["abcde","abcdf","abcdg"],["abcd?","abc??","ab???","ab??","??cde","???dg"]),[3,3,3,0,1,1])
print(solution(["gggba","gggab","ggefe","ggff"],["???ba","???ab","?????","gg???","???f"]),[1,1,3,3,1])
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["????o", "fr???", "fro???", "pro?", "fro??"]),[2, 4, 1, 0, 3])