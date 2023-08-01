# 209. Minimum Size Subarray Sum
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        s = 0
        n = len(nums)
        m = n
        l = 0
        r = -1
        min_sum = 0
        while(r<n-1 or s>=target):
            if(s>=target):
                m = min(m,(r-l+1))
                min_sum = s
                s-=nums[l]
                l+=1
            else:
                r+=1
                s+=nums[r]
                
        return m if min_sum>=target else 0
    
