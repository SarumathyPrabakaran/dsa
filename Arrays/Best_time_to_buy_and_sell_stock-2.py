'''
122. Best Time to Buy and Sell Stock II

Input: prices = [7,1,5,3,6,4]
Output: 7

'''

class Solution:
    def maxProfit(self, prices:list) -> int:
        max_pro = 0
        l = 0
        r = 1
        while(l<r and r<len(prices)):
            k = (prices[r]-prices[l])
            max_pro+= k if k>0 else 0
            l+=1
            r+=1
        return max_pro
