import sys

sys.stdin = open("sample_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    pars = input()

    bars = 0
    stack_count = 0

    for i in range(len(pars)):
        if pars[i] == '(':
            stack_count += 1
        if pars[i] == ')':
            if pars[i-1] == '(':
                stack_count -= 1
                bars += stack_count
            else:
                stack_count -= 1
                bars += 1

    print("#{}".format(test_case),bars)
    # ///////////////////////////////////////////////////////////////////////////////////
