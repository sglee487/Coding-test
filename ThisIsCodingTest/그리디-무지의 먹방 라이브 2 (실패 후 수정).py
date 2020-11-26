# https://programmers.co.kr/learn/courses/30/lessons/42891
# 어차피 일일이 해야된다는 것을 알았으면, 어떻게 효율적으로 시뮬할수 있을 지 생각하자..

import heapq

def solution(food_times, k):
    if sum(food_times) <= k: return -1
    q = []
    n = len(food_times)
    for i in range(n):
        heapq.heappush(q,(food_times[i],i+1))
    cycle = 0
    while (q[0][0]-cycle) * n <= k:
        outfood = heapq.heappop(q)
        k -= ((outfood[0]-cycle) * n)
        n -= 1
        cycle = outfood[0]

    q.sort(key=lambda x:x[1])
    print(k)
    return q[k%n][1]

print(solution([3, 1, 2],5),1)