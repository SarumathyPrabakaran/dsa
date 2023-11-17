

'''
2306. Naming a Company

Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6

Approach: Create a dictionary of sets to group words by their first character from the 'ideas' list.
Calculate the number of distinct pairs of words with no common suffix by iterating through the dictionary and using set operations.

'''
from collections import defaultdict


class Solution:
    def distinctNames(self, ideas: list) -> int:
        words = defaultdict(set)
        for i in ideas:
            words[i[0]].add(i[1:])
        res =0
        for w in words:
            for c in words:
                if w==c:
                    continue
                common = 0
                for l in words[w]:
                    if l in words[c]:
                        common+=1
                dis1 = len(words[w])-common
                dis2 = len(words[c])-common
                res+=dis1*dis2
        print(res)
        return res


s = Solution()
s.distinctNames(["coffee","donuts","time","toffee"])
