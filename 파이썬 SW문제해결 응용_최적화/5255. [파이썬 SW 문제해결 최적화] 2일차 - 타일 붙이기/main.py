import sys

sys.stdin = open("sample_input.txt", "r")

def inputbox(n):
    if n <= 3:
        return BoxResultList[n]

    for i in range(4,n+1):
        if BoxResultList[i] != -1: continue
        BoxResultList[i] = BoxResultList[i-1] + 2*BoxResultList[i-2] + BoxResultList[i-3]
    return BoxResultList[n]

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 6
    else:
        return inputbox(n-3) + 2*inputbox(n-2) + inputbox(n-1)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    BoxResultList = [-1] * (N+1)
    BoxResultList[0] = 0
    BoxResultList[1] = 1
    BoxResultList[2] = 3
    BoxResultList[3] = 6
    result = inputbox(N)
    # print(result)
    # print(BoxResultList)

    print("#{}".format(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
