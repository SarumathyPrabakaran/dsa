'''
554. Brick Wall
Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2

'''
from collections import defaultdict
class Solution:
    def leastBricks(self, wall):
        border = defaultdict(int)
        max_crosses = 0

        for w in wall:
            s = 0
            for j in w[:-1]:
                s += j
                border[s] += 1
                max_crosses = max(max_crosses, border[s])

        return len(wall) - max_crosses
