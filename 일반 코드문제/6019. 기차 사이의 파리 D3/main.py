import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    D, A, B, F = map(int, input().split())
    result = round(D / (A+B) * F,6)

    print("#{0} {1:.9f}".format(test_case,result))
    # ///////////////////////////////////////////////////////////////////////////////////
