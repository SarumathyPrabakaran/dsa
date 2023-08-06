'''
347. Top K Frequent Elements

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

'''
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums:list, k: int) -> list:
        
        d = defaultdict(int)
        for i in nums:
                d[i]+=1
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1],reverse= True))

        return list(sorted_dict.keys())[:k]

sl = Solution()
print(sl.topKFrequent([1,1,1,2,2,3],2))