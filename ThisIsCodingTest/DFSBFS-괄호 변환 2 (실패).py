# https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    if p == '' or p == None: return ''
    gal = 0
    right = True
    for i,c in enumerate(p):
        if c == '(':
            gal += 1
        elif c == ')':
            gal -= 1
        if gal == 0:
            return str(solution(p[:i])) + str(solution(p[i:]))
        elif gal < 0:
            right = False
            break
    if not right:
        return '(' + solution(p[1:-1]) + ')'
    return p

print(solution("(()())()"),"(()())()")
print(solution(")("),"()")
print(solution("()))((()"),"()(())()")