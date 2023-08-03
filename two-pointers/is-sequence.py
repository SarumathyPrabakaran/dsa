'''

392. Is Subsequence

Input: s = "abc", t = "ahbgdc"
Output: true


'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="": return True
        if t=="":return False
        l = 0
        r = 0
        n1 = len(s)
        n2 = len(t)
        while(l<n1 and r<n2):
            if s[l]==t[r]:
                l+=1
            r+=1
        
        if l!=n1-1 and t[r-1]!=s[l-1] or(l<n1 and r==n2):
                return False
        else:
                return True


s = Solution()
print(s.isSubsequence("abc","ahbdfcg"))