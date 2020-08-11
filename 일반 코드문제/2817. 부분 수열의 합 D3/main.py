import sys

sys.stdin = open("sample_input.txt", "r")

def allPartSum(i,K,S,R):
    global result
    if i == -1:
        if S == K:
            result += 1
        return
    if S > K: return
    if R < K: return
    allPartSum(i - 1, K, S + numbers[i], R)
    allPartSum(i - 1, K, S,R - numbers[i])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    result = 0
    # 시간 초과
    # for i in range(1 << len(numbers)):
    #     if sum([numbers[j] for j in range(len(numbers)) if i & (1 << j)]) == K: result += 1

    # 4,138 ms
    # for i in range(1 << len(numbers)):
    #     temp_sum = 0
    #     for j in range(len(numbers)):
    #         if i & (1 << j):
    #             temp_sum += numbers[j]
    #         if temp_sum > K: break # 2,197 ms
    #     if temp_sum == K: result += 1
    #     temp_sum = 0

    # 626 ms
    allsum = sum(numbers)
    allPartSum(N-1,K,0,allsum)

    print("#{}".format(test_case), result)
    # ///////////////////////////////////////////////////////////////////////////////////
