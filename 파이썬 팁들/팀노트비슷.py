# https://github.com/ndb796/Python-Competitive-Programming-Team-Notes

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

''' Rotate a matrix by 90 degree '''
def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res

print(rotate_a_matrix_by_90_degree(a))


# 우선순위 큐 내장함수
import heapq
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 이진탐색 내장함수
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x)) # 2
print(bisect_right(a,x)) # 4

# 이진탐색을 이용한 원소 갯수 세기
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4)) # 2

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 6


# 단어 뒤집기
print("abcde"[::-1])

# 단어 교체
print("abc???".replace('?','a'))
print("abc???".replace('?','z'))
res = count_by_range(['aabeef','abbdef','abcdef','abcdee','abcfzz','abdffe'],"abc???".replace('?','a'),"abc???".replace('?','z'))
print(res)

# 최단경로(다익스트라 dijkstra) 알고리즘
# 최단경로-미래도시
import sys

import heapq

sys.stdin = open("최단경로-미래 도시.txt", "r")

def dijkstra(start):
    Q = []
    distance = [987654321] * (N+1)
    distance[start] = 0
    heapq.heappush(Q,(0,start))
    while Q:
        dist, now = heapq.heappop(Q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(Q,(cost,i[0]))
    return distance


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append((b,1))
        graph[b].append((a,1))
    X, K = map(int, input().split())
    dis1 = dijkstra(1)
    disk = dijkstra(K)
    print(dis1[K] + disk[X] if (dis1[K] + disk[X]) < 987654321 else -1)