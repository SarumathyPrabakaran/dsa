

'''
17. Letter Combinations of a Phone Number

Input: digits = "23"

2: abc
3: def
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


'''


class Solution:
    def letterCombinations(self, digits: str):
        d = {2: "abc", 3:"def", 4: "ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv",9:"wxyz"}
        ans = []
        
        def backtrack(res, j):
            
            if j==len(digits):
                if res=='':
                    pass
                else:
                    ans.append(res) 
                return 
            for i in d[int(digits[j])]:
                backtrack(res+i,j+1)

        backtrack('',0)
        return ans   