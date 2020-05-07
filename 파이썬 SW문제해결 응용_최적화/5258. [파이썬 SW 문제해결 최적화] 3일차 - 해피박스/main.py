import sys

sys.stdin = open("sample_input.txt", "r")

def knapsack():
    for i in range(n+1):
        K[i][0] = 0
    for w in range(W+1):
        K[0][w] = 0

    for i in range(1,n+1):
        for w in range(1,W+1):
            if weight[i] > w:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(K[i-1][w - weight[i]] + value[i], K[i-1][w])
    return K[n][W]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    weight = [0] * (M+1)
    value = [0] * (M + 1)
    for i in range(M):
        weight[i+1],value[i+1] = map(int, input().split())

    n = M
    W = N
    K = [[0] * (W+1) for _ in range(M+1)]
    result = knapsack()

    print("#{}".format(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
