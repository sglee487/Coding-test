import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    S1, S2 = input().split()
    # a b c d e f g h i j k l m n o p q r s t u v w x y z
    # print(ord('a')) # 97
    # print(ord('z')) # 122
    S1o = [0] * (122-97 + 1)
    S2o = [0] * (122 - 97 + 1)
    for s1,s2 in zip(S1,S2):
        S1o[ord(s1)-97] += 1
        S2o[ord(s2) - 97] += 1
    count = 0
    if S1o == S2o: count += 1
    for i in range(len(S1),len(S2)):
        S2o[ord(S2[i - len(S1)]) - 97] -= 1
        S2o[ord(S2[i]) - 97] += 1
        if S1o == S2o: count += 1

    print("#{}".format(test_case),count)
    # ///////////////////////////////////////////////////////////////////////////////////
