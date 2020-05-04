import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    se = []
    for _ in range(N):
        st, et = map(int, input().split())
        se.append((st,et))

    se = sorted(se,key=lambda tu: tu[1])

    result = [se[0]]
    j = 0
    for i in range(len(se)):
        if se[i][0] >= se[j][1]:
            result.append(se[i])
            j = i

    print("#{}".format(test_case),len(result))

    # ///////////////////////////////////////////////////////////////////////////////////
