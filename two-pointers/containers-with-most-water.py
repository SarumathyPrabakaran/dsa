
'''
11. Container With Most Water

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49


'''

class Solution:
    def maxArea(self, height: list) -> int:
        l= 0
        r = len(height)-1
        ma = 0
        while(l<r):
            sm = l if height[l]<height[r] else r
            now = (r-l)*(height[sm])
            if(now>ma):
                ma = now
            if(l==sm): l+=1
            else: r-=1
        return ma
    
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))