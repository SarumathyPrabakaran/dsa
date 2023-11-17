


# Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list4) -> int: 
        d = set()
        n = len(nums)
        t = 0
        i =0
        while(t<n):
            if nums[i] in d:
                nums.pop(i)
                
            else:
                d.add(nums[i])
                i+=1
            t+=1

sl = Solution()
sl.removeDuplicates([1,1,2,2,3,3,3,4])