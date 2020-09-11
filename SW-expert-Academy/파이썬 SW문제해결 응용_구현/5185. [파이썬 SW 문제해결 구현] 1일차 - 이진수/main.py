import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, ST = input().split()

    str = ''
    for c in ST:
        if c == '0': str += '0000'
        if c == '1': str += '0001'
        if c == '2': str += '0010'
        if c == '3': str += '0011'
        if c == '4': str += '0100'
        if c == '5': str += '0101'
        if c == '6': str += '0110'
        if c == '7': str += '0111'
        if c == '8': str += '1000'
        if c == '9': str += '1001'
        if c == 'A': str += '1010'
        if c == 'B': str += '1011'
        if c == 'C': str += '1100'
        if c == 'D': str += '1101'
        if c == 'E': str += '1110'
        if c == 'F': str += '1111'


    print("#{}".format(test_case),str)

    # ///////////////////////////////////////////////////////////////////////////////////
