import sys

sys.stdin = open("정렬-카드 정렬하기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(int(input()))
    numbers.sort()
    total_sum = 0
    for i,n in enumerate(numbers):
        if i >= 2:
            total_sum += total_sum + n
        else:
            total_sum += n
    print(total_sum)