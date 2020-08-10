import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 다른사람꺼 보고 참고함..
    Days = input()
    bitsmasks = [[0] * 16 for _ in range(len(Days))]
    for i in range(16):
        # 처음 A와 초기 담당자 설정
        if i & 1 << 0 and i & (1 << (ord(Days[0]) - 65)): # 초기 A와 1번째 날짜 담당자 다 가지고 있으면
            bitsmasks[0][i] = 1

    for i in range(1,len(Days)):
        pb = 1 << (ord(Days[i]) - 65)
        for j in range(16):
            if pb & j:
                for k in range(16):
                    if j & k:
                        # print(pb,i,j,k,bitsmasks[i][j],bitsmasks[i-1][k])
                        bitsmasks[i][j] = (bitsmasks[i][j] + bitsmasks[i-1][k]) % 1000000007
                # print(pb,j)
                # print(*bitsmasks, sep='\n')
                # print()

    # print(*bitsmasks,sep='\n')
    print("#{}".format(test_case),sum(bitsmasks[-1]) % 1000000007)
    # ///////////////////////////////////////////////////////////////////////////////////

# 0000 0
# 0001 1 A
# 0010 2 B
# 0011 3 AB
# 0100 4 C
# 0101 5 AC
# 0110 6 BC
# 0111 7 ABC
# 1000 8 D
# 1001 9 AD
# 1010 10 BD
# 1011 11 ABD
# 1100 12 CD
# 1101 13 ACD
# 1110 14 BCD
# 1111 15 ABCD