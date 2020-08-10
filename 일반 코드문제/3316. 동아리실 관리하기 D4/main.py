import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    Days = input()
    print(Days)

    possible = ['A','B','C','D','AB','AC','AD','BC','BD','CD','ABC','ABD','ACD','BCD','ABCD']
    results = [1]
    result = 1

    prev_stats = []

    day_possible = 0
    for p in possible:
        if Days[0] in p and 'A' in p:
            day_possible += 1
            prev_stats.append(p)
    result *= day_possible
    result %= 1000000007

    prev_d = Days[0]
    for d in Days[1:]:


    print(result)

    print("#{}".format(test_case))
    # ///////////////////////////////////////////////////////////////////////////////////
