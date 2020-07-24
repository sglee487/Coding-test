import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    name_len_list = set()
    for _ in range(N):
        name = input()
        name_len_list.add((name,len(name)))

    name_len_list = list(name_len_list)
    name_len_list.sort(key= lambda x : (x[1],x[0]))

    print("#{}".format(test_case))
    for e in name_len_list:
        print(e[0])

    # ///////////////////////////////////////////////////////////////////////////////////
