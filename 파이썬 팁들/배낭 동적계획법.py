# 파이썬 SW문제해결 응용_최적화 - 03 동적계획법의 적용

# 배낭 문제에 동적 계획법을 적용해서 상향식으로 최적해를 구하는 알고리즘
# 배낭의 무게 W
# i: 배낭에 넣을 물건을 나타내는 값(1...n)
# n: 물건의 개수
# 리턴: K[n][W]
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