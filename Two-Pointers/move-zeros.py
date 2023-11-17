#283. Move Zeroes

'''
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

'''

class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        t = 0
        i = 0
        while(t<n):
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
            t+=1
sl = Solution()
nums = [0,1,0,3,12]
sl.moveZeroes(nums)
print(nums)
