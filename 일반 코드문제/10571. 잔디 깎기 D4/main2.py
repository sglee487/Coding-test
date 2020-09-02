# 258 ms
import sys

sys.stdin = open("input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())

    Row_max = [0] * N
    H = [[0] * M for _ in range(N)]
    for i in range(N):
        H[i] = list(map(int, input().split()))
        Row_max[i] = max(H[i])

    # print(*H,sep='\n')

    Col_max = [0] * M
    HR = [0 for _ in range(M)]
    for i, c in enumerate(zip(*H)):
        HR[i] = list(c)
        Col_max[i] = max(HR[i])

    # 왼쪽, 아래, 오른쪽, 위
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]

    # print(Row_max,Col_max)
    result = True
    for r in range(N):
        for c in range(M):
            if H[r][c] < Row_max[r] and H[r][c] < Col_max[c]:
                result = False
                break
        if not(result): break

    result_string = "YES"
    if not(result): result_string = "NO"
    print("#{}".format(test_case), result_string)
    # ///////////////////////////////////////////////////////////////////////////////////
