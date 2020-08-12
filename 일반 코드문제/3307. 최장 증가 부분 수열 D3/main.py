import sys

sys.stdin = open("sample_input3.txt", "r")

### https://wayhome25.github.io/cs/2017/04/15/cs-16/
def binary_search(target):
    # data.sort()
    start = 0
    end = len(C) - 1

    while start <= end:
        mid = (start + end) // 2

        if C[mid] <= target:
            start = mid + 1
        else:
            end = mid -1

    return start

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 파이썬 SW문제해결 응용_최적화 - 04 동적계획법의 활용
    # 알고보니 5262. [파이썬 S/W 문제해결 최적화] 4일차 - 정렬된 부분 집합 D4 와 같은문제...
    N = int(input())
    numbers = list(map(int, input().split()))

    C = [2**31] * (N+1)
    C[0] = 0
    LIS = [1] * N

    c_index = 0
    for i,n in enumerate(numbers):
        c_index = binary_search(n)
        C[c_index] = n
        LIS[i] = c_index
        # print("i :",i,", n :",n, ", c_index :",c_index)
        # print("C :",C)
        # print("LIS :",LIS)

    print("#{}".format(test_case), max(LIS))
    # ///////////////////////////////////////////////////////////////////////////////////
