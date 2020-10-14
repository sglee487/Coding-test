# https://programmers.co.kr/learn/courses/30/lessons/60062
def solution(n, weak, dist):
    wn = len(weak)
    wcl = [0] * n
    for w in weak:
        wcl[w] = 1
    expandwcl = wcl[:] + wcl[:] + wcl[:]
    print(expandwcl)
    si = len(wcl)
    for w in weak:
        if sum(expandwcl[si+w:si+w+dist[-1]+1]) == wn:
            return 1
    answer = 0
    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]),2)
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]),1)