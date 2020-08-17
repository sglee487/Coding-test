import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    otl = list(map(int, input().split()))

    otl = sorted(otl,reverse=True)
    sale = [otl[i] for i in range(len(otl)) if ((i+1) % 3) == 0 ]

    print("#{}".format(test_case),sum(otl) - sum(sale))
    # ///////////////////////////////////////////////////////////////////////////////////