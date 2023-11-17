# 1. Two Sum


from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            if(target-nums[i] in nums):
                l = nums.index(target-nums[i])
                if(i==l):
                    continue
                return i, l
            
sl = Solution()
print(sl.twoSum([2,7,11,15],9))

