import sys

sys.stdin = open("input.txt", "r")

def allPartSum(i,K,S,R):
    global lowest_H, B
    if i == -1:
        if S >= K and lowest_H > S:
            lowest_H = S
        return
    if S > lowest_H: return
    if R < K: return
    allPartSum(i - 1, K, S + H[i], R)
    allPartSum(i - 1, K, S,R - H[i])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    lowest_H = 200000

    allsum = sum(H)
    allPartSum(N-1,B,0,allsum)


    print("#{}".format(test_case), lowest_H - B)
    # ///////////////////////////////////////////////////////////////////////////////////
