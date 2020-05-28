import sys

sys.stdin = open("sample_input.txt", "r")

def isAvailable(a,c,k):
    count = 0
    for i in range(len(a)-1):
        if a[i+1] - a[i] > c:
            count += a[i+1] - (a[i] + c)
            a[i+1] = a[i] + c
        # print(a,i,c,count,k)
        if count > k:
            return False
    for i in range(len(a)-1,0,-1):
        if a[i-1] - a[i] > c:
            count += a[i-1] - (a[i] + c)
            a[i-1] = a[i] + c
        # print(a, i, c, count, k)
        if count > k:
            return False
    return True

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    s = 0
    e = max(A)-min(A)
    while s < e:
        c = (s+e) // 2
        if isAvailable(A[:],c,K):
            e = c
        else:
            s = c + 1

    print("#{}".format(test_case),s)
    # ///////////////////////////////////////////////////////////////////////////////////
