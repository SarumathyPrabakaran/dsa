'''
215. Kth Largest Element in an Array

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Approach: Use min heap and control the length of the heap to k. to account for O(log k) complexity,


'''
from collections import heapq

class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]