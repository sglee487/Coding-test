from typing import List

def dfs(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] > target or nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[right] < target or nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return dfs(nums, target)

print(Solution.search(None,[4,5,6,7,0,1,2],0),4)
print(Solution.search(None,[4,5,6,7,0,1,2],3),-1)
print(Solution.search(None,[1],0),-1)