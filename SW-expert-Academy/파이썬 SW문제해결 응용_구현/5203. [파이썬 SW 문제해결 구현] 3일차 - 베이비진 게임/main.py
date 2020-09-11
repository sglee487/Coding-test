import sys

sys.stdin = open("sample_input.txt", "r")

def is_run_or_triplet(count_list):
    for i in range(len(count_list)):
        if (count_list[i] >= 1) and (count_list[i+1] >= 1) and (count_list[i+2] >= 1):
            return True
        if (count_list[i] >= 3):
            return True
    return False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    full_list = list(map(int, input().split()))

    fpc = [0] * 12
    spc = [0] * 12

    result = 0
    for i in range(len(full_list)):
        if i % 2 == 0:
            fpc[full_list[i]] += 1
            if is_run_or_triplet(fpc):
                result = 1
                break
        else:
            spc[full_list[i]] += 1
            if is_run_or_triplet(spc):
                result = 2
                break

    print("#{}".format(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
