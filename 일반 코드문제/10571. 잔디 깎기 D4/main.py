# 387 ms
import sys

sys.stdin = open("input2.txt", "r")

def is_safe(now_r,now_c):
    now_e = H[now_r][now_c]
    y_bool = True
    x_bool = True

    # 아래 위
    for i in [1,3]:
        new_y = now_r + dy[i]
        new_x = now_c + dx[i]
        while 0 <= new_y < N and 0 <= new_x < M:
            if H[new_y][new_x] > now_e:
                y_bool = False
                break
            new_y += dy[i]
            new_x += dx[i]
        if not(y_bool): break

    # 왼쪽 오른쪽
    for i in [0,2]:
        new_y = now_r + dy[i]
        new_x = now_c + dx[i]
        while 0 <= new_y < N and 0 <= new_x < M:
            if H[new_y][new_x] > now_e:
                x_bool = False
            new_y += dy[i]
            new_x += dx[i]
        if not(x_bool): break

    return y_bool or x_bool

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())

    H = [[0] * M for _ in range(N)]
    for i in range(N):
        H[i] = list(map(int, input().split()))

    # print(*H,sep='\n')

    # 왼쪽, 아래, 오른쪽, 위
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]

    result = True
    for r in range(N):
        for c in range(M):
            if not(is_safe(r,c)):
                result = False
        if not(result): break

    result_string = "YES"
    if not(result): result_string = "NO"
    print("#{}".format(test_case), result_string)
    # ///////////////////////////////////////////////////////////////////////////////////
