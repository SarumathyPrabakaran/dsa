from typing import *

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        ans = 0
        g = len(requests)
        for i in range((2**g)):
            indeg = [0 for _ in range(n)]
            c = (bin(i)).count('1')
            
            if(c<=ans):
                continue
                
            ind = 0
            
            while(i>0):
                if(i&1):            
                    indeg[requests[ind][0]]-=1
                    indeg[requests[ind][1]]+=1
                ind+=1
                i = i>>1
        
            if (all(k==0 for k in indeg)):
                ans = c
        return ans


sl = Solution()
print(sl.maximumRequests(5,[[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))