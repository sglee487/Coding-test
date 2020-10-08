def solution(s):
    if len(set(s)) == 1: return 0
    beauti = 0
    for i in range(len(s)):
        lastbuti = 0
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                beauti += lastbuti
            else:
                beauti += j-i
                lastbuti = j-i
            print(s[i],s[j],i,j,beauti)
    return beauti

# print(solution("baby"),9)
# print(solution("oo"),0)
# print(solution("ab"),1)
# print(solution("abb"),3)
# print(solution("abbb"),6)
# print(solution("abab"),8)
# print(solution("abca"),9)
# print(solution("abcb"),9)
# print(solution("abce"),10)
# print(solution("abace"),10)
print(solution("aabaa"),12)
print(solution("aba"),3)
print(solution("abaa"),6)
print(solution("abbca"))