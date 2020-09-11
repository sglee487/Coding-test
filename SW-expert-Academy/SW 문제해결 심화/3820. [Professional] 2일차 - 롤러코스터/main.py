import sys
import itertools
import functools
sys.stdin = open("sample_input.txt", "r")

def compare_rail(x,y):
    com1 = y[0]*(x[0]+x[1]) + y[1]
    com2 = x[0]*(y[0]+y[1]) + x[1]
    print(x,y,com1,com2,com1-com2)
    return com1-com2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    rail = [0] * (N)
    for i in range(N):
        a,b = map(int, input().split())
        rail[i] = (a,b)

    # rail.sort(key=lambda x:x[1]-x[0])
    cmp = functools.cmp_to_key(compare_rail)
    print(rail)
    rail.sort(key=cmp)
    print(rail)
    v = 1
    # vc = list(itertools.permutations(rail,r=5))
    # print(vc)
    for a,b in rail:
        v = ((a*v) + b) % 1000000007
        print(v)
    # v=1
    # for r in vc:
    #     v = 1
    #     print(r)
    #     for a, b in r:
    #         v = (a * v) + b
    #         print(v)
    # print(v % 1000000007)

    print("#{}".format(test_case),v % 1000000007)
    # ///////////////////////////////////////////////////////////////////////////////////
