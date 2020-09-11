import sys

sys.stdin = open("sample_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    st = input()
    # print(st)

    pen = True
    for i in range(len(st)//2):
        if st[i] != st[-(i+1)] and st[i] != '?' and st[-(i+1)] != '?':
            # print(i,-(i+1),st[i],st[-(i+1)])
            pen = False

    # print(pen)
    if pen: ex = 'Exist'
    else: ex = 'Not exist'

    print("#{}".format(test_case),ex)
    # ///////////////////////////////////////////////////////////////////////////////////
