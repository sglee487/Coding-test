# https://programmers.co.kr/learn/courses/30/lessons/60060
from collections import defaultdict


def reversestr(string):
    word = [''] * len(string)
    for i in range(len(string)):
        word[i] = string[len(string)-1-i]
    return ''.join(word)

def find_qu_index(string):
    si, ei = 0, len(string)-1
    result = 0
    while si <= ei:
        mid = (si + ei) // 2
        if string[mid] == '?':
            result = mid
            ei = mid-1
        else:
            si = mid+1
    return result

def find_partsameword_firstindex(words,qword,qi):
    si, ei = 0, len(words) - 1
    result = -1
    while si <= ei:
        mid = (si + ei) // 2
        if len(qword) > len(words[mid]):
            si = mid + 1
        elif len(qword) < len(words[mid]):
            ei = mid - 1
        else:
            if words[mid][:qi] == qword[:qi]:
                result = mid
                ei = mid - 1
            else:
                si = mid + 1
    return result

def find_partsameword_lastindex(words,qword,qi):
    si, ei = 0, len(words) - 1
    result = -1
    while si <= ei:
        mid = (si + ei) // 2
        if len(qword) > len(words[mid]):
            si = mid + 1
        elif len(qword) < len(words[mid]):
            ei = mid - 1
        else:
            if words[mid][:qi] == qword[:qi]:
                result = mid
                si = mid + 1
            else:
                ei = mid - 1
    return result

def find_word_count(qs,words,dict,r):
    for qword in qs:
        qi = find_qu_index(qword)
        pssi = find_partsameword_firstindex(words,qword,qi)
        psli = find_partsameword_lastindex(words,qword,qi)
        if not r:
            dict[qword][1] = psli - pssi + 1 if psli != -1 else 0
        else:
            dict[reversestr(qword)][1] = psli - pssi + 1 if psli != -1 else 0


def solution(words, queries):
    qicdict = defaultdict(list)
    preqs_r = []
    sufqs = []
    for i, e in enumerate(queries):
        qicdict[e] = [i,0]
        if e[0] == '?':
            preqs_r.append(reversestr(e))
        elif e[-1] == '?':
            sufqs.append(e)
    words_r = [reversestr(c) for c in words]
    # print(sorted(words + queries,key=lambda x: (len(x),str(x))))
    # print(sorted(words_r + preqs_r,key=lambda x: (len(x),str(x))))
    # print(sorted(words + sufqs,key=lambda x: (len(x),str(x))))
    # print(sorted(words,key=lambda x: (len(x),str(x))))
    find_word_count(sorted(sufqs,key=lambda x: (len(x),str(x))),sorted(words,key=lambda x: (len(x),str(x))),qicdict,False)
    find_word_count(sorted(preqs_r,key=lambda x: (len(x),str(x))),sorted(words_r,key=lambda x: (len(x),str(x))),qicdict,True)
    # print(qicdict)
    answer = [0] * len(queries)
    for v in qicdict.values():
        answer[v[0]] = v[1]
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]),[3, 2, 4, 1, 0])