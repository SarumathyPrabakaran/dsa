# 345. Reverse Vowels of a String
'''
Input: s = "leetcode"
Output: "leotcede"

'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s)-1
        vow_r, vow_l = False, False
        while(r>=l):
            if(s[l].lower() not in 'aeiou'):
                l+=1
            else:
                vow_l = True
            if(s[r].lower() not in 'aeiou'):
                r-=1
            else:
                vow_r = True
            if(vow_l and vow_r):
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
                vow_r, vow_l = False, False
        return ''.join(s)
sl = Solution()
print(sl.reverseVowels("leetcode"))