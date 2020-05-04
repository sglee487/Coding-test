import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())

    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w = sorted(w, reverse=True)
    t = sorted(t)

    result = 0
    for we in w:
        for te in t:
            if te >= we:
                result += we
                t.remove(te)
                break
            # print(t, te, we, result)

    print("#{}".format(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
