from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        K = k
        k = 0
        for n in nums:
            if n == 1:
                if k > 0: return False
                k = K
            else:
                k -= 1
        return True

print(Solution.kLengthApart(None,[1,0,0,0,1,0,0,1],2),True)
print(Solution.kLengthApart(None,[1,0,0,1,0,1],2),False)
print(Solution.kLengthApart(None,[1,1,1,1,1],0),True)
print(Solution.kLengthApart(None,[0,1,0,1],1),True)