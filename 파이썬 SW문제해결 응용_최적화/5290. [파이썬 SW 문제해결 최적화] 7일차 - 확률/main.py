import sys
import itertools

sys.stdin = open("sample_input.txt", "r")

t = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, t + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    nl = list(range(10))
    pr = 10**N
    pe = 1
    for i in range(10,10-N,-1):
        pe *= i
    result = pe/pr
    # result = len(list(itertools.permutations(nl,N)))/len(list(itertools.product(nl,repeat=N)))

    print("#{}".format(test_case),"{:.5f}".format(result))
    # ///////////////////////////////////////////////////////////////////////////////////
