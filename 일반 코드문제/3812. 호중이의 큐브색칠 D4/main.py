import sys

sys.stdin = open("sample_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    X, Y, Z, A, B, C, N = map(int, input().split())
    # print(X, Y, Z, A, B, C, N)

    colors = [0] * N

    x_end, y_end, z_end = (X-A) // N, (Y-B) // N, (Z-C) // N
    x_end_re, y_end_re, z_end_re = (X-A) % N, (Y-B) % N, (Z-C) % N
    x_zero, y_zero, z_zero = A // N, B // N, C // N
    x_zero_re, y_zero_re, z_zero_re = A % N, B % N, C % N

    x = [x_end + x_zero] * N
    for i in range(0, x_end_re):
        x[i] += 1
    for i in range(1, x_zero_re+1):
        x[i] += 1

    y = [y_end + y_zero] * N
    for i in range(0, y_end_re):
        y[i] += 1
    for i in range(1, y_zero_re+1):
        y[i] += 1

    z = [z_end + z_zero] * N
    for i in range(0, z_end_re):
        z[i] += 1
    for i in range(1, z_zero_re+1):
        z[i] += 1

    xy = [0] * N
    for i in range(N):
        for j in range(N):
            xy[(i+j) % N] += x[i] * y[j]

    xyz = [0] * N
    for i in range(N):
        for j in range(N):
            xyz[(i+j) % N] += xy[i] * z[j]

    # print(x,y,z,xy,xyz)

    print("#{}".format(test_case),*xyz)
    # ///////////////////////////////////////////////////////////////////////////////////
