import sys
import heapq

sys.stdin = open("정렬-카드 정렬하기.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Nsh = []
    result = 0
    for _ in range(N):
        heapq.heappush(Nsh,int(input()))
    while len(Nsh) > 1:
        one = heapq.heappop(Nsh)
        two = heapq.heappop(Nsh)
        result += one + two
        heapq.heappush(Nsh,one+two)
    print(result)