import sys

sys.stdin = open("sample_input.txt", "r")

def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)
    # return A

def partition(A,l,r):
    p = A[l]
    i = l+1
    j = r
    while i <= j:
        while(i <= j and A[i] <=p): i += 1
        while(i <=j and A[j] >= p): j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    L = list(map(int, input().split()))
    quickSort(L, 0, len(L)-1)

    print("#{}".format(test_case),L[N//2])

    # ///////////////////////////////////////////////////////////////////////////////////
