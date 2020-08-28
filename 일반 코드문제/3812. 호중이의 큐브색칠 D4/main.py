import sys

sys.stdin = open("sample_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    X, Y, Z, A, B, C, N = map(int, input().split())

    colors = [0] * N
    garo = [0] * N

    x_end, y_end, z_end = (X // N) * N, (Y // N) * N, (Z // N) * N
    print(x_end,y_end,z_end)
    not_remain_x = (X // N) * Y * Z
    not_remain_y = (X-x_end) * (Y // N) * Z
    not_remain_z = (X-x_end) * (Y-y_end) * (Z // N)
    print(not_remain_x,not_remain_y,not_remain_z)
    colors = [not_remain_x + not_remain_y + not_remain_z] * N


    print(colors)
    print("#{}".format(test_case))
    # ///////////////////////////////////////////////////////////////////////////////////
