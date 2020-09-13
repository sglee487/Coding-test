from collections import defaultdict

def solution(boxes):
    boxnum = len(boxes)
    prodic = defaultdict(int)

    for p1,p2 in boxes:
        prodic[p1] += 1
        prodic[p2] += 1

    nowboxnum = 0
    for h in prodic.values():
        nowboxnum += h // 2

    return boxnum-nowboxnum

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
print(solution([[1, 2], [3, 4], [5, 6]]))
print(solution([[1, 2], [2, 3], [3, 1]]))