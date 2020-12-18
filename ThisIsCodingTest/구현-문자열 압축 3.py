# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    N = len(s)
    shortestlen = N
    for al in range(1,(N//2)+1):
        string = ''
        prevstr = s[:al]
        prevlen = 1
        for i in range(al,N,al):
            if prevstr == s[i:i+al]:
                prevlen += 1
            else:
                if prevlen == 1:
                    string += prevstr
                else:
                    string += str(prevlen) + prevstr
                prevlen = 1
                prevstr = s[i:i+al]
        if prevlen == 1:
            string += prevstr
        else:
            string += str(prevlen) + prevstr
        shortestlen = min(shortestlen,len(string))
        # print(string)
    # print(shortestlen)

    return shortestlen

print(solution("aabbaccc"),7)
print(solution("ababcdcdababcdcd"),9)
print(solution("abcabcdede"),8)
print(solution("abcabcabcabcdededededede"),14)
print(solution("xababcdcdababcdcd"),17)