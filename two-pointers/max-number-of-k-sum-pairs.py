'''
1679. Max Number of K-Sum Pairs

Input: nums = [1,2,3,4], k = 5
Output: 2


'''

class Solution:
    def maxOperations(self, nums: list, k: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        c = 0
        r = n-1
        while(l<r):
            s = nums[l]+nums[r]
            if s==k:
                
                c+=1
                l+=1
                r-=1
            elif(k>s):
                l+=1
            else:
                r-=1
        return c


s = Solution()
print(s.maxOperations([1,2,3,4],5))