import sys

sys.stdin = open("sample_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    A, B = input().split()

    si = 0
    match_num = 0
    i = 0
    while i <= len(A) - len(B):
        j = len(B) - 1
        while j >= 0:
            if A[i + j] != B[j]:
                k = len(B)-2
                while k >= 0:
                    if A[i + j] == B[k]: break
                    k -= 1
                if k != -1:
                    i += len(B) - k - 1
                else:
                    i += len(B)
                break
            j -= 1

        if j == -1:
            match_num += 1
            i += len(B)

    result = len(A) - (len(B) * match_num) + match_num

    print("#{}".format(test_case), result)
    # ///////////////////////////////////////////////////////////////////////////////////
