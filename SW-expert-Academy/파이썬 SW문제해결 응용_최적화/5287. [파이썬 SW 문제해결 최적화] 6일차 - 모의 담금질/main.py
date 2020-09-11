import sys
import math
import random

sys.stdin = open("sample_input.txt", "r")

def cost(value):
    return value * random.uniform(0.8, 5.0)

t = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, t + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    T, T_end, k = map(float, input().split())

    iter_count = 0
    # cost_pre = float('inf')  # 이전 비용
    cost_pre = 10000
    T = T
    while T > T_end:  # T_end가 될 때까지 반복
        cost_new = cost(cost_pre)  # 비용 계산
        iter_count += 1
        diff = cost_new - cost_pre # 새로운 비용과 이전 비용의 차이
        if diff < 0 or math.exp(-diff / T) > random.uniform(0, 1):
            cost_pre = cost_new  # 비용이 감소하거나 확률이 랜덤 값보다 더 크면 비용 갱신
        T = T * k  # k : cooling factor

    print("#{}".format(test_case), iter_count)
    # ///////////////////////////////////////////////////////////////////////////////////
