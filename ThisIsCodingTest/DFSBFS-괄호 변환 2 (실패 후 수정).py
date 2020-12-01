# https://programmers.co.kr/learn/courses/30/lessons/60058

def balanced_index(w):
    stack = 0
    for i, c in enumerate(w):
        if c == '(': stack += 1
        elif c == ')': stack -= 1
        if stack == 0: return i

def is_proper(w):
    stack = 0
    for i, c in enumerate(w):
        if c == '(':
            stack += 1
        elif c == ')':
            stack -= 1
        if stack < 0: return False
    return True

def solution(p):
    if p == '': return ''
    bi = balanced_index(p)
    u = p[:bi+1]
    print(p[:bi])
    print(p[:bi+1])
    v = p[bi+1:]
    if is_proper(u):
        return u + solution(v)
    else:
        answer = ''
        answer += '('
        answer += solution(v)
        answer += ')'
        ur = ''
        for c in u[1:-1]:
            if c == '(': ur += ')'
            if c == ')': ur += '('
        answer += ur
        return answer


print(solution("(()())()"),"(()())()")
print(solution(")("),"()")
print(solution("()))((()"),"()(())()")