'''

128. Longest Consecutive Sequence

Input: nums = [100,4,200,1,3,2]
Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Approach: Find the start element 1,100,400. and check if the consecutive exists.

'''


class Solution:
    def longestConsecutive(self, nums: list) -> int:
        nums = set(nums)
        m = 0
        for i in nums:
            if i-1 not in nums:
                c=1
                while(i+c in nums):
                    c+=1
                m = max(c,m)
        return m
