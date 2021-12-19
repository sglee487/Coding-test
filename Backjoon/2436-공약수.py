# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2436-공약수-2.txt", "r")

input = sys.stdin.readline

a, b = map(int, input().split())

def get_dividers(n):
    dividers = []
    for e in range(1, int(n**(1/2))+1):
        if n % e == 0:
            dividers.append(e)
            if e ** 2 != n:
                dividers.append(n//e)
    return sorted(dividers)

def is_suro(a,b):
    for n in range(2, int((min(a,b)**(1/2)))+1):
        if a % n == 0 and b % n == 0:
            return False
    return True

suro = []
bal = get_dividers(b//a)
N = len(bal)
suro.append(bal[N//2]-2)
suro.append(bal[N//2]-1)
suro.append(bal[N//2])
suro.append(bal[N//2]+1)
suro.append(bal[N//2]+2)
result = []
for i in range(N//2,N):
    if is_suro(bal[i], bal[N-i-1]):
        result.append(bal[N-i-1]*a)
        result.append(bal[i]*a)
        break
print(*result)
