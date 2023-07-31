# 238. Product of Array Except Self
from typing import *
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        res = [0]*len(nums)
        for i in range(0,len(nums)):
            res[i] = pre
            pre*=nums[i]
        post = 1
        for j in range(len(nums)-1,-1,-1):
            res[j]*=post
            post*=nums[j]
        return res
    

sl = Solution()
print(sl.productExceptSelf([1,2,3,4]))