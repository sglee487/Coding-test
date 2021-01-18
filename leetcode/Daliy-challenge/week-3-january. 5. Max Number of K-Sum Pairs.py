from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums, k)
        lp = 0
        rp = len(nums)-1
        count = 0
        while lp < rp:
            tsum = nums[lp] + nums[rp]
            if tsum > k:
                rp -= 1
            elif tsum < k:
                lp += 1
            else:
                count += 1
                rp -= 1
                lp += 1
        return count


print(Solution.maxOperations(Solution,[1,2,3,4],5),2)
print(Solution.maxOperations(Solution,[3,1,3,4,3],6),1)