'''
523. Continuous Subarray Sum

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Approach: Have a table with columns remainder and index. if again the remainder occurs then a k multiple is added to the remainder.'''

class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        d = {0: -1}
        tot = 0
        
        for i,e in enumerate(nums):
            tot+=e
            r = tot%k
            if r not in d:
                d[r] = i
            elif i-d[r]>=2:
                return True
        return False