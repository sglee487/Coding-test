# https://programmers.co.kr/learn/courses/30/lessons/60058
def is_balances(s):
    return s.count('(') == s.count(')')

def is_proper(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0: return False
    if count != 0: return False
    return True

def solution(p):
    # print('p',p)
    if p == '' or p == None: return ''
    for i in range(1,len(p)+1):
        if is_balances(p[:i]):
            u = p[:i]
            v = p[i:]
            if is_proper(u):
                # print('u,v',u,v)
                return u + solution(v)
            else:
                answer = '('
                answer += solution(v)
                answer += ')'
                u = u[1:-1]
                tu = ''
                for c in u:
                    if c == '(': tu += ')'
                    if c == ')': tu += '('
                answer += tu
                return answer



print(solution("(()())()"),"(()())()")
print(solution(")("),"()")
print(solution("()))((()"),"()(())()")