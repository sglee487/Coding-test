import sys

sys.stdin = open("sample_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    A, B = input().split()

    si = 0
    match_num = 0
    i=0
    j=0
    while i < len(A):
        print(i)
        while A[i] == B[j] and j < len(B):
            i += 1
            j += 1
            print(i,j)
            if i == len(A) or j == len(B): break
        if i == len(A) or j == len(B): break
        if j == len(B):
            match_num += 1
        else:
            while A[i] != B[j]:
                j -= 1
                if j == -1: break
            i -= j
        i += 1
        j = 0
    print(match_num)




    print("#{}".format(test_case))
    # ///////////////////////////////////////////////////////////////////////////////////
