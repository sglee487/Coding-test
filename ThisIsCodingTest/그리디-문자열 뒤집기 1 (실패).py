import sys

sys.stdin = open("그리디-문자열 뒤집기.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    S = input()
    result = 0
    flag = True
    prev_c = S[0]
    for c in S[1:]:
        if prev_c != c:
            if flag:
                flag = False
            else:
                flag = True
                result += 1

    print(result)