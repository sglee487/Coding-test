import sys

# http://cd4761.blogspot.com/2017/02/trie-1.html
# http://cd4761.blogspot.com/2017/03/trie-2.html
# https://www.geeksforgeeks.org/pattern-searching-using-suffix-tree/
# http://blog.naver.com/PostView.nhn?blogId=kks227&logNo=221028710658
# https://swexpertacademy.com/main/talk/solvingTalk/boardCommuView.do?searchCondition=COMMU_DETAIL-COMMU_TITLE-NICK_NAME_TAG&commuId=AXAuybMapTADFAXq&searchKeyword=5254&orderBy=DATE_DESC&pageSize=10&pageIndex=1&&&&&&


def LongestCommonPrefix(a,b):
    i=0
    while i < min(len(a),len(b)):
        if a[i] != b[i]: break
        i += 1
    return i

sys.stdin = open("sample_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 그냥 배열로 하니까 안됨.
    # 진짜 접미어 트리 배열 써야 하는 듯..

    inp = input().split()
    n = int(inp[0])
    s = inp[1]

    print(s)
    print("n :",n)
    # 그냥 배열로 하니까 안됨.
    # 진짜 접미어 트리 배열 써야 하는 듯..
    sps = set()
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            sps.add(s[i:j])
    sp = sorted(list(sps))
    print(sp)

    A = [[0] * 2 for _ in range(len(s))]
    for i in range(len(s)):
        A[i][0] = i
        A[i][1] = s[i:]
    # print(A)
    A = sorted(A,key=lambda a:a[1])
    print(A)
    LCP = [0] * len(A)
    LCP[0] = 0
    for i in range(1,len(A)):
        LCP[i] = LongestCommonPrefix(A[i-1][1],A[i][1])
    print(LCP)

    resultc = ''
    resultl = 0
    for i in range(len(A)):
        suffix_index = A[i][0]
        curstr = A[i][1]
        if n > len(curstr):
            n += LCP[i] - len(curstr)
        else:
            resultc = curstr[0]
            resultl = len(curstr[:(n+LCP[i])])
            break

    print("#{}".format(test_case),resultc,resultl)

    # ///////////////////////////////////////////////////////////////////////////////////
