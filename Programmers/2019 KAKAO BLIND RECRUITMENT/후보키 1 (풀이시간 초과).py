from itertools import combinations

def solution(relation):
    answer = 0
    rowlen = len(relation)
    collen = len(relation[0])
    proved = []
    il = list(range(collen))
    for i in range(1,collen+1):
        for comb in combinations(il,i):
            collist = [e for e in comb]
            if collist in proved: continue
            tuples = set()

            for r in relation:
                tmp = []
                for j, e in enumerate(r):
                    if j in collist:
                        tmp.append(e)
                tuples.add(tuple(tmp))
            if len(tuples) == rowlen:
                answer += 1
                proved.append(set(collist))
    deletesetindex = set()
    for i in range(len(proved)):
        for j in range(i+1,len(proved)):
            if proved[i].issubset(proved[j]):
                deletesetindex.add(j)
    answer = len(proved) - len(deletesetindex)
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]),2)