import sys

sys.stdin = open("s_input.txt", "r")

from itertools import combinations

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    numbers = list(map(int, input().split()))
    com_set = set()
    for s in list(combinations(numbers,3)):
        com_set.add(sum(s))

    print("#{}".format(test_case),sorted(com_set,reverse=True)[4])

    # ///////////////////////////////////////////////////////////////////////////////////
