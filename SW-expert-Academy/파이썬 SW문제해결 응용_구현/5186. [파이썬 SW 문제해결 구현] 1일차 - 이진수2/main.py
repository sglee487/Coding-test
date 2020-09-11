import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = float(input())

    str = ''

    count = 1

    while count != 13:
        N = N * 2
        if N > 1:
            str = str + '1'
            N -= 1
        elif N < 1:
            str = str + '0'
        else:
            str = str + '1'
            break
        count += 1
    if count == 13: str = 'overflow'

    print("#{}".format(test_case), str)

    # ///////////////////////////////////////////////////////////////////////////////////
