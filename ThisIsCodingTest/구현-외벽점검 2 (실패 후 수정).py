# https://programmers.co.kr/learn/courses/30/lessons/60062
# https://github.com/ndb796/python-for-coding-test/blob/master/12/8.py
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(len(weak)):
        weak.append(n+weak[i])
    answer = len(dist) + 1
    for start in range(length):
        for freinds in permutations(dist, len(dist)):
            count = 1
            position = weak[start] + freinds[count-1]
            for i in range(start, start+length):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i] + freinds[count-1]
            answer = min(answer,count)
    if answer > len(dist):
        return -1
    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]),2)
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]),1)