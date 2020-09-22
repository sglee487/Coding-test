# 파이썬 SW문제해결 응용_최적화 - 07 정수론과 최적화
# 소수 검사 알고리즘
import math
def is_prime2_1(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for d in range(3, int(math.sqrt(n)+1),2):
        if n % d == 0: return False
    return True

# 순열, 조합, 중복순열, 중복조합
# https://juhee-maeng.tistory.com/91
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

# 소수 확인
def isPrimeNumber(number):
    if number <= 1:
        return False
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True