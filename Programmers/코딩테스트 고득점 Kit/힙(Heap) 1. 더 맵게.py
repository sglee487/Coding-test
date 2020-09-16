import heapq

def solution(scoville, K):
    Q = scoville[:]
    heapq.heapify(Q)
    count = 0
    while not(all(e >= K for e in Q)) and len(Q) > 1:
        heapq.heappush(Q, heapq.heappop(Q) + 2 * heapq.heappop(Q))
        count += 1
    if len(Q) == 1 and Q[0] < K:
        return -1
    else:
        return count

print(solution([1, 2, 3, 9, 10, 12],7),2)