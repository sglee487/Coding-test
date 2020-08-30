import sys

sys.stdin = open("sample_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    X, Y, Z, A, B, C, N = map(int, input().split())
    print(X, Y, Z, A, B, C, N)

    colors = [0] * N
    garo = [0] * N

    x_end, y_end, z_end = ((X-A) // N) * N + A, ((Y-B) // N) * N + B, ((Z-C) // N) * N + C
    x_zero, y_zero, z_zero = A-((A // N) * N), B-((B // N) * N), C-((C // N) * N)
    print(x_end,y_end,z_end)
    print(x_zero,y_zero,z_zero)
    axis = int()
    gongtong = 0
    if x_end - x_zero == 0 and x_end - x_zero == 0 and x_end - x_zero == 0:
        axis = -1
    elif x_end - x_zero != 0:
        gongtong = (((x_end - x_zero) * (Y) * (Z)) // N)
        axis = 0
    elif y_end - y_zero != 0:
        gongtong = (((X) * (y_end - y_zero) * (Z)) // N)
        axis = 1
    elif z_end - z_zero != 0:
        gongtong = (((X) * (Y) * (z_end - z_zero)) // N)
        axis = 2

    colors = [gongtong] * N

    print(colors)
    print("#{}".format(test_case))
    # ///////////////////////////////////////////////////////////////////////////////////
