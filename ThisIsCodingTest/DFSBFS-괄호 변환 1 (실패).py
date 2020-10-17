# https://programmers.co.kr/learn/courses/30/lessons/60058

def isbalanced(p):
    counto = 0
    countc = 0
    for c in p:
        if c == '(': counto += 1
        if c == ')': countc += 1
    return counto == countc

def isalright(p):
    stack = 0
    for c in p:
        if c == '(': stack += 1
        if c == ')': stack -= 1
        if stack < 0: return False
    if stack > 0: return False
    return True

def dfs(p):
    for s in range(len(p)+1):
        if isbalanced(p[:s]):
            return apart(p[:s],p[s:])

def apart(u,v):
    if isalright():
        pass

def solution(p):
    if p == '': return p

    return

print(solution("(()())()"),"(()())()")
print(solution(")("),"()")
print(solution("()))((()"),"()(())()")