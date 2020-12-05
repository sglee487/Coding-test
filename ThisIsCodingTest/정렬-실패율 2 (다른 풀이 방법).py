from collections import defaultdict

# https://programmers.co.kr/learn/courses/30/lessons/42889
# https://github.com/ndb796/python-for-coding-test/blob/master/14/3.py
def solution(N, stages):
    length = len(stages)
    answer = []
    for i in range(1,N+1):
        fails = stages.count(i)
        answer.append((i,fails/length))
        length -= fails
    answer.sort(key=lambda x:-x[1])
    answer = [e[0] for e in answer]

    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]),[3,4,2,1,5])
print(solution(4,[4,4,4,4,4]),[4,1,2,3])