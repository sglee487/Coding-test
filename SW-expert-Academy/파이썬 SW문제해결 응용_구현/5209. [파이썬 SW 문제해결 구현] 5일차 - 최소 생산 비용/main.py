import sys

sys.stdin = open("sample_input.txt", "r")

def permutation(order, k, n, subsum):
    global minsum
    if subsum >= minsum:
        return

    if k == n:
        if subsum < minsum:
            minsum = subsum
    else:
        check = [False] * n
        for i in range(k):
            check[order[i]] = True

        for i in range(n):
            if check[i] == False:
                order[k] = i
                permutation(order, k+1,n,subsum + V[k][i])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    minsum = 99*N

    permutation([0]*N,0,N,0)

    print("#{}".format(test_case),minsum)

    # ///////////////////////////////////////////////////////////////////////////////////
