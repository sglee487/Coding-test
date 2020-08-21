import sys

sys.stdin = open("input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    Percents = []
    for _ in range(N):
        Percents.append([*map(lambda x:x/100,map(int, input().split()))])

    print(Percents)

    print("#{}".format(test_case))
    # ///////////////////////////////////////////////////////////////////////////////////
