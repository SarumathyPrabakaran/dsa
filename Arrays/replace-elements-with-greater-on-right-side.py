'''
1299. Replace Elements with Greatest Element on Right Side

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Approach: reverse the array and start from the last. you need to  condiser current and prev max alone.
'''

class Solution:
    def replaceElements(self, arr: list) -> list:
        rev, maximum = arr[::-1], -1
        for i in range(0,len(rev)):
            rev[i], maximum = maximum, max(rev[i],maximum)
            print(maximum)
            
        
        return rev[::-1]