import sys

sys.stdin = open("sample_input.txt", "r")

def allPartSum(i,K,S,R):
    global result
    print(i,K,S,R)
    if i == 0:
        if S == K:
            result += 1
        return
    if S > K: return
    if R < K: return
    allPartSum(i - 1, K, S + jiphap[i], R)
    allPartSum(i - 1, K, S,R - jiphap[i])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    jiphap = list(range(N+1))
    S = 0
    allsum = sum(jiphap)
    result = 0
    allPartSum(N,K,0,allsum)
    print("#{}".format(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////
