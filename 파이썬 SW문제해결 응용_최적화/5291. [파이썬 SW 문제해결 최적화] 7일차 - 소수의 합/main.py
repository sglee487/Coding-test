import sys
import math
sys.stdin = open("sample_input.txt", "r")

def is_prime2_1(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for d in range(3, int(math.sqrt(n)+1),2):
        if n % d == 0: return False
    return True

t = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, t + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    a, b = map(int, input().split())
    result = 0
    for i in range(a+1,b):
        if is_prime2_1(i): result += i

    print("#{}".format(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////
