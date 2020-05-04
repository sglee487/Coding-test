import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M):
        i, num = map(int, input().split())
        numbers.insert(i,num)
    print("#{}".format(test_case),numbers[L])

    # ///////////////////////////////////////////////////////////////////////////////////
