import sys

sys.stdin = open("input2.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, K = map(int, input().split())

    customers = sorted(list(map(int, input().split())))

    bbang = 0

    customer_index = 0

    result = "Possible"
    if min(customers) == 0:
        result = "Impossible"
    else:
        for time in range(1, max(customers)+1):
            if time % M == 0:
                bbang += K
            while customers[customer_index] == time:
                bbang -= 1
                customer_index += 1
                if bbang < 0:
                    result = "Impossible"
                    break
                if customer_index == N:
                    break


    print("#{}".format(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////
