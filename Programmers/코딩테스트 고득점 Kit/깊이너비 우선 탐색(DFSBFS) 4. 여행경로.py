from collections import deque

def solution(tickets):
    answer = []
    N = len(tickets)
    Q = deque()
    Q.append(('ICN',['ICN'],tickets[:]))
    while Q:
        now, stopover, tickets = Q.popleft()
        if len(stopover) == N+1: answer.append(stopover)
        for i, (a,b) in enumerate(tickets):
            if a == now: Q.append((b,stopover + [b],tickets[:i]+tickets[i+1:]))
        # print(Q)
    return sorted(answer)[0]

print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]),['ICN', 'JFK', 'HND', 'IAD'])
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]),['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'])
print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]),['ICN', 'B', 'ICN', 'A'])