import heapq
from collections import deque

def solution(jobs):
    jq = deque(sorted(jobs))
    jh = []
    time = 0
    total_delay = 0
    working = []
    while working or jq or jh:
        if working:
            working[0][0] = working[0][0] - 1
            if working[0][0] <= 0:
                total_delay += (time - working[0][1])
                working.pop()

        while jq and time == jq[0][0]:
            s, l = jq.popleft()
            heapq.heappush(jh,[l,s])

        if not working and jh:
            working.append(heapq.heappop(jh))

        time += 1

    return (total_delay) // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]),9)
print(solution([[0,3],[4,3],[10,3]]),3)
print(solution([[0,10],[2,3],[9,3]]),9)
print(solution([[1,10],[3,3],[10,3]]),9)
print(solution([[0,10]]),10)
print(solution([[0,10],[4,10],[5,11],[15,2]]),15)