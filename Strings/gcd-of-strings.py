class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        def gcd(n,m):
            rem = n%m
            if(rem==0):
                return m
            else:
                return gcd(m,rem)
        n = gcd(len(str1), len(str2))
        return str1[:n]
    
sl = Solution()
print(sl.gcdOfStrings("ABCABC","ABC"))