import sys

sys.stdin = open("sample_input.txt", "r")

# https://ggodong.tistory.com/90
# https://herong.tistory.com/entry/SWEA-3813-%EA%B7%B8%EB%9E%98%EB%8F%84-%EC%88%98%EB%AA%85%EC%9D%B4-%EC%A0%88%EB%B0%98%EC%9D%B4-%EB%90%98%EC%96%B4%EC%84%9C%EB%8A%94

def isAvailable(p):
    now = 1
    cont = 0
    for i in range(1,lenS+1):
        # print("i,now,cont,p,S[i]",i,now,cont,p,S[i])
        if S[i] <= p:
            cont += 1
        else:
            cont = 0
        if cont == K[now]:
            cont = 0
            now += 1
            if now > lenK:
                break
    return now > lenK

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    lenS,lenK = map(int, input().split())
    S = list(map(int, input().split()))
    K = list(map(int, input().split()))
    S.insert(0,0)
    K.insert(0, 0)
    print(S,K)

    s = min(S)
    e = max(S)
    while s<e:
        m = (s+e) // 2
        print("s,m,e",s,m,e)
        if (isAvailable(m)):
            e = m
        else:
            s = m + 1
    print(s)

    print("#{}".format(test_case),s)
    # ///////////////////////////////////////////////////////////////////////////////////
