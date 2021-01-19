# 계산 시간이 길어서 개선해야될것 같긴 하다.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        N = len(s)
        for length in range(N,-1,-1):
            for start_index in range(N-length+1):
                parts = s[start_index:start_index+length]
                # print(length,parts,parts[::-1])
                if parts == parts[::-1]:
                    result = parts
                    break
            if result: break
        return result


print(Solution.longestPalindrome(None,"babad"),"bab")
print(Solution.longestPalindrome(None,"cbbd"),"bb")
print(Solution.longestPalindrome(None,"a"),"a")
print(Solution.longestPalindrome(None,"ac"),"a")