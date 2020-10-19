import sys

sys.stdin = open("DP-1로 만들기.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    numbers = [1]
    step = 0
    si = 0
    found = False
    while not found:
        for n in numbers[si:]:
            if n == N:
                found = True
                break
            numbers.append(n*5)
            numbers.append(n*3)
            numbers.append(n*2)
            numbers.append(n+1)
        si = si + 4**(step)
        step += 1
    print(step-1)