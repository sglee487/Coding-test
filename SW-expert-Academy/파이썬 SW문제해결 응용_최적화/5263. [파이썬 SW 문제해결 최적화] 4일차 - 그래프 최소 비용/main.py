import sys

sys.stdin = open("sample_input.txt", "r")

def AllPairsShortest(D):
    for k in range(0, N):
        for i in range(0, N):
            if i == k: continue
            for j in range(0,N):
                if j == k or j == i: continue
                if D[i][k] == 0 or D[k][j] == 0:
                    D[i][j] = D[i][j]
                elif D[i][j] == 0:
                    D[i][j] = D[i][k] + D[k][j]
                else:
                    D[i][j] = min(D[i][k] + D[k][j], D[i][j])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    AllPairsShortest(D)
    dup = []
    for k in D:
        for i in k:
            dup.append(i)

    print("#{}".format(test_case),max(dup))
    # ///////////////////////////////////////////////////////////////////////////////////
