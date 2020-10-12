import sys

sys.stdin = open("그리디-곱하기 혹은 더하기.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    S = input()
    result = int(S[0])
    for c in S[1:]:
        n = int(c)
        if n <= 1 or result <= 1:
            result += n
        else:
            result *= n

    print(result)