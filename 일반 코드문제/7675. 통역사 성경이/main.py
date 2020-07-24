import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    sentences = list(input().split())

    namecounts = [0] * N
    sentindex = 0
    sentcount = 0
    name_flag = False
    for sentence in sentences:
        if 'A' <= sentence[0] <= 'Z':
            name_flag = True
            for c in sentence[1:]:
                if not('a' <= c <= 'z') and not(c == '!' or c == '.' or c == '?'):
                    name_flag = False
                if not(name_flag):
                    break
        if name_flag:
            sentcount += 1
        if sentence[-1] == '!' or sentence[-1] == '.' or sentence[-1] == '?':
            namecounts[sentindex] = sentcount
            sentcount = 0
            sentindex += 1
            name_flag = False

    print("#{}".format(test_case),*namecounts)

    # ///////////////////////////////////////////////////////////////////////////////////
