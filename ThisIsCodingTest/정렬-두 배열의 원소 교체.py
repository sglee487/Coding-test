import sys

sys.stdin = open('정렬-두 배열의 원소 교체.txt', "r")

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

rightindex = N-1
for i in range(N):
    if A[i] < B[rightindex]:
        A[i] = B[rightindex]
        rightindex -= 1
        K -= 1
    if rightindex < 0 or K == 0:
        break
print(sum(A))