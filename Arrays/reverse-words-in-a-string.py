

# 151. Reverse Words in a String

'''

Input: s = "the sky is blue"
Output: "blue is sky the"

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        # l = []
        # l = s.split(" ")
        # k  = ""
        # print(l)
        # for i in l[::-1]:
        #     if i =='':
        #         continue
        #     k+=(i.strip())
        #     k+=" "
        
        # return k.strip()

        return " ".join(reversed(s.split()))
    
sl = Solution()
print(sl.reverseWords("a good   example"))