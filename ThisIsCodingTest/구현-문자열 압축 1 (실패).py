# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    prl =[[] for _ in range(len(s)+1)]
    for i in range(1,len(s)+1):
        for j in range(0,len(s),i):
            prl[i].append(s[j:j+i])
    psel = [[] for _ in range(len(s)+1)]
    for i in range(1,len(prl)):
        count = 0
        j=i
        while j < len(prl[i]):
            for k in range(j+1,len(prl[i])):
                if prl[i][j] == prl[i][k]:
                    count += 1
                else: break
            if count == 1:
                psel[i].append(prl[i])
            # else:
                # psel[i].append(str(count) + prl[i])
            j = k-1
    print(psel)
    return 