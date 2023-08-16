'''
334. Increasing Triplet Subsequence


Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

'''


class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
                