'''

3. Longest Substring Without Repeating Characters

Approach: Sliding Window.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        l = 0
        r = 0
        a = set()
        ma = 0
        while(l<=r and r<len(s)):
            if s[r] in a:
                while(s[r] in a):
                    a.remove(s[l])
                    l+=1
            ma = max(ma,r-l+1)
            a.add(s[r])
            r+=1
        return ma