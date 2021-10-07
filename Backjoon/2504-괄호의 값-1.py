import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("2504-괄호의 값-5.txt", "r")

input = sys.stdin.readline

gul = input().strip()
# print(gul)

def gulho(gul):
    stack = []
    for c in gul:
        # print(c)
        if c in ('(','['):
            stack.append(c)
        elif c == ')':
            if not stack: return 0
            elif stack[-1] == '(':
                stack.pop()
                stack.append('2')
            elif len(stack) >= 2 and stack[-1].isdigit() and stack[-2] == '(':
                last:str = stack.pop()
                stack.pop()
                stack.append(str(int(last) * 2))
            else:
                return 0
        elif c == ']':
            if not stack: return 0
            elif stack[-1] == '[':
                stack.pop()
                stack.append('3')
            elif len(stack) >= 2 and stack[-1].isdigit() and stack[-2] == '[':
                last:str = stack.pop()
                stack.pop()
                stack.append(str(int(last) * 3))
            else:
                return 0
        while len(stack)>=2 and stack[-1].isdigit() and stack[-2].isdigit():
            one = int(stack.pop())
            two = int(stack.pop())
            stack.append(str(one+two))
        # print(stack)
    # print(stack)
    if not stack or len(stack) != 1 or not stack[0].isdigit():
        return 0
    else:
        return int(stack[0])

print(gulho(gul))