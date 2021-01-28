def convert(num):
    ALPAS = 'abcdefghijklmnopqrstuvwxyzAAAA'
    if num == 0:
        return ''
    elif num > 25:
        return convert(num-25) + 'z'
    else:
        return ALPAS[num]

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        num = k-n
        result = convert(num)
        result = 'a' * (n-len(result)) + result
        return result


print(Solution.getSmallestString(None,3,27),"aay")
print(Solution.getSmallestString(None,5,73),"aaszz")
print(Solution.getSmallestString(None,3,28),"aaz")
print(Solution.getSmallestString(None,3,29),"abz")
print(Solution.getSmallestString(None,3,30),"acz")