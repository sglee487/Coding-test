# https://programmers.co.kr/learn/courses/30/lessons/42891
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    foodheap = []
    for i, f in enumerate(food_times,1):
        heapq.heappush(foodheap,(f,i))

    cycle = 0
    while (foodheap[0][0]-cycle) * len(foodheap) <= k:
        k -= (foodheap[0][0]-cycle) * len(foodheap)
        cycle += (foodheap[0][0]-cycle)
        heapq.heappop(foodheap)
    foodheap.sort(key= lambda x:x[1])
    return foodheap[k%len(foodheap)][1]

print(solution([3, 1, 2],5),1)