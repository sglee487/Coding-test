# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    N = len(s)
    lowestlen = len(s)
    for l in range(1,(N//2)+1):
        prev = s[0:0+l]
        count = 1
        compressed = ''
        for i in range(l,N,l):
            if prev == s[i:i+l]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[i:i+l]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        lowestlen = min(lowestlen,len(compressed))
        # print(compressed)

    return lowestlen

print(solution("aabbaccc"),7)
print(solution("ababcdcdababcdcd"),9)
print(solution("abcabcdede"),8)
print(solution("abcabcabcabcdededededede"),14)
print(solution("xababcdcdababcdcd"),17)