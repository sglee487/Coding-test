from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    orsets = list()
    menudic = defaultdict(set)
    for o in orders:
        orsets.append(set(o))

    for i in range(len(orsets)):
        for j in range(i+1,len(orsets)):
            l = sorted(list(orsets[i] & orsets[j]))
            if len(l) <= 1: continue
            t = []
            for k in range(2, len(l) + 1):
                c = combinations(l, k)
                t.extend(c)
            for e in t:
                menudic[''.join(e)].add(i)
                menudic[''.join(e)].add(j)

    lis = [[] for _ in range(21)]
    cc = []
    answer = []
    for k,v in menudic.items():
        if len(k) not in course: continue
        lis[len(v)].append(k)
    for i in range(20,1,-1):
        t = []
        for s in lis[i]:
            if len(s) not in cc:
                t.append(len(s))
                answer.append(s)
        for te in t:
            cc.append(te)
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))