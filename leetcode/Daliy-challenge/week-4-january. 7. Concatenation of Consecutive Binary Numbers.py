class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = ""
        for i in range(1, n+1):
            indexbin = "{0:b}".format(i)
            result += indexbin
        return int(result,2) % (int(1e9) + 7)



print(Solution.concatenatedBinary(None,1),1)
print(Solution.concatenatedBinary(None,3),27)
print(Solution.concatenatedBinary(None,12),505379714)