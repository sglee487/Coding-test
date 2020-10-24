# 입력 사이에 공간이 있을때
list(map(int,input().split()))

# 입력이 너무 많을 때
import sys
sys.stdin = open("최단경로-전보.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에
# 또는
import sys
T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, K = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 입력 사이에 공간이 없을때
list(input())
board = [input() for _ in range(N)]

# 행렬 만들기
visited = [[0] * N for _ in range(N)]
ds = [[[9999999,9999999,9999999,9999999] for _ in range(N)] for _ in range(N)]
graph = [[] * n for _ in range(n)]

for A, B in path:
    graph[A].append(B)
    graph[B].append(A)

# 리스트 원소 거르기
a = [1,2,3,4,5]
print([i for i in a if i % 2 == 0 ])
# print([i if i % 2 == 0 for i in a ]) X
print([i for i in a if i % 2 == 0 or i % 3 == 0])
print([i if i % 2 == 0 else 9 for i in a])
# print([i for i in a if i % 2 == 0 else 9 ]) X

# 리스트 리스트 만들기
etl = [[] for _ in range(60000)]
te = []
for s,e in routes:
    te.append((s,'in'))
    te.append((e,'out'))
    etl[s+30000].append(e)

# 정렬 기준 방법
room_numbers = sorted(room_numbers, key=lambda x: -x[1])

# 행렬 뒤집기
N, M = map(int, input().split())
HR = [0 for _ in range(N)]
for i, c in enumerate(zip(*H)):
    HR[i] = list(c)

# 행렬 방향
# 왼쪽, 아래, 오른쪽, 위
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
for i in range(4):
    new_y = start_y + dy[i]
    new_x = start_x + dx[i]
    if isSafe(new_y, new_x) and (new_y, new_x) not in stack:
        DFS(new_y, new_x)
# 아래, 우측아래, 우측, 우측위, 위, 좌측위, 좌측, 좌측아래
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
for d in range(8):
    y = r + dy[d]
    x = c + dx[d]
    if 0 <= x < N and 0 <= y < N:
        if board[y][x] == 0:
            click_zero(y, x)
        board[y][x] = 'C'
for d in range(8):
    x,y = r_q,c_q
    while 1<=x and x<=n and 1<=y and y<=n:
        ans += 1
        x+=dx[d]
        y+=dy[d]
        if (x,y) in block:
            break
    return (ans-8)

# 딕셔너리, 큐
from collections import deque
from collections import defaultdict

# 우선순위 큐(힙)
# https://python.flowdas.com/library/heapq.html
# https://medium.com/@yhmin84/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-priority-queue-%EB%A5%BC-%EC%9C%84%ED%95%9C-heapq-%EB%AA%A8%EB%93%88-%EC%82%AC%EC%9A%A9%EB%B2%95-b33c4e0ef2b1
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