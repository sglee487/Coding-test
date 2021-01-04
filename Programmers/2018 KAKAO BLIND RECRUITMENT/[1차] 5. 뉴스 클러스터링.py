from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1list = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1list.append(str1[i] + str1[i+1])
    str2list = []
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2list.append(str2[i] + str2[i+1])
    result = 0
    if len(str1list) == 0 and len(str2list) == 0:
        result = 1
    else:
        allset = set(str1list) | set(str2list)
        counter1 = Counter(str1list)
        counter2 = Counter(str2list)
        gyo = 0
        hap = 0
        for s in allset:
            gyo += min(counter1[s],counter2[s])
            hap += max(counter1[s],counter2[s])
        result = gyo / hap
    return int(result * 65536)

print(solution("FRANCE","french"),16384)