import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    _ = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = set(A + B)
    result = len(A) + len(B) - len(C)
    print("#{}".format(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////
