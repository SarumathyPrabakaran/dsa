# 1431. Kids With the Greatest Number of Candies
'''

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]

'''
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        def find_boolean(a):
            return (a+extraCandies)>=m
        l = []
        l= list(map(find_boolean, candies))
        return l
    
s = Solution()
print(s.kidsWithCandies([2,3,5,1,3],3))