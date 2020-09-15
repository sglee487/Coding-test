from collections import deque

def solution(priorities, location):
    inprinter = deque()
    for i,p in enumerate(priorities):
        inprinter.append((i,p))

    counter = 1
    while inprinter:
        out = True
        cand = inprinter.popleft()
        for i,p in inprinter:
            if p > cand[1]:
                inprinter.append(cand)
                out = False
                break
        if out:
            if cand[0] == location:
                break
            counter += 1

    return counter

print(solution([2, 1, 3, 2],2),1)
print(solution([1, 1, 9, 1, 1, 1],0),5)