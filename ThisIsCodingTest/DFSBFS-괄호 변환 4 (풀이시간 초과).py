# https://programmers.co.kr/learn/courses/30/lessons/60058

def is_balanced(p):
    stack = 0
    for c in p:
        if c == '(':
            stack += 1
        elif c == ')':
            stack -= 1
    return stack == 0

def is_right(p):
    stack = 0
    for c in p:
        if c == '(':
            stack += 1
        elif c == ')':
            stack -= 1
        if stack < 0:
            return False
    return stack == 0


def solution(w):
    if w == '': return ''
    index = 1
    while index < len(w):
        if is_balanced(w[:index]):
            break
        index += 1
    u = w[:index]
    v = w[index:]
    if is_right(u):
        return u + solution(v)
    else:
        ts = '('
        ts = ts + solution(v)
        ts = ts + ')'
        u = u[1:-1]
        tu = ''
        for e in u:
            if e == '(':
                tu = tu + ')'
            elif e == ')':
                tu = tu + '('
        return ts + tu


print(solution("(()())()"),"(()())()")
print(solution(")("),"()")
print(solution("()))((()"),"()(())()")