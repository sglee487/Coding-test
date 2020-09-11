import sys

sys.stdin = open("sample_input.txt", "r")

# https://wayhome25.github.io/cs/2017/04/15/cs-16/
def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return start

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    inline = list(map(int, input().split()))
    N = inline[0]
    A = inline[1:]
    LIS = [1] * N
    C = [1001] * (N+1)
    C[0] = 0
    for i in range(len(A)):
        input_index = binary_search(A[i],C)
        C[input_index] = A[i]
        LIS[i] = input_index

    print("#{}".format(test_case),max(LIS))
    # ///////////////////////////////////////////////////////////////////////////////////
