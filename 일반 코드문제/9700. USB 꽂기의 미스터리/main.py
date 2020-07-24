import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    p, q = map(float, input().split())

    s1 = (1 - p) * q
    s2 = (p * (1 - q) * q)
    # print(s1,s2)
    result_string = 'YES' if s1 < s2 else 'NO'

    print("#{}".format(test_case),result_string)

    # ///////////////////////////////////////////////////////////////////////////////////
