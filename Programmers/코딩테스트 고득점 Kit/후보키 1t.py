from itertools import combinations
def solution(relation):
    answer = 0
    all = list()
    uniqeIndex = []
    if len(relation) > 0:
        colSize = len(relation[0])
        rowSize = len(relation)
        for i in range(1, colSize + 1):
            all.extend([set(k) for k in combinations([j for j in range(colSize)], i)])
        for comb in all:
            vaildSet = set()
            for row in range(rowSize):
                temp = ''
                for col in comb:
                    temp += relation[row][col]
                vaildSet.add(temp)
            if len(vaildSet) == rowSize:
                uniqeIndex.append(comb)
        print(uniqeIndex)
        delSet = set()
        for stdMinElem in uniqeIndex:
            for idx, compMinElem in enumerate(uniqeIndex):
                if stdMinElem.issubset(compMinElem) and stdMinElem != compMinElem:
                    delSet.add(uniqeIndex.index(compMinElem))
        answer = len(uniqeIndex)-len(delSet)
        print(delSet)
    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]),2)