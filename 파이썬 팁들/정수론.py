# 파이썬 SW문제해결 응용_최적화 - 07 정수론과 최적화
# 소수 검사 알고리즘
import math
def is_prime2_1(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for d in range(3, int(math.sqrt(n)+1),2):
        if n % d == 0: return False
    return True