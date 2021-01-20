from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')':
                if not stack: return False
                if stack[-1] != '(': return False
                stack.pop()
            elif c == ']':
                if not stack: return False
                if stack[-1] != '[': return False
                stack.pop()
            elif c == '}':
                if not stack: return False
                if stack[-1] != '{': return False
                stack.pop()
        if not stack: return True
        else: return False


print(Solution.isValid(None,"()"),True)
print(Solution.isValid(None,"()[]{}"),True)
print(Solution.isValid(None,"(]"),False)
print(Solution.isValid(None,"([)]"),False)
print(Solution.isValid(None,"{[]}"),True)