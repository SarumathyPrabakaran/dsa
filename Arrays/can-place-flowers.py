
'''

605. Can Place Flowers

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true'''


from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        one = False
        for i,a in enumerate(flowerbed):
            if a:
                one = True
            elif(i+1<len(flowerbed)):
                if not one and not flowerbed[i+1]:
                    n-=1
                    one = True
                else:
                    one = False
        if not flowerbed[i] and not one:
            n-=1
        return True if n<=0 else  False