# 1-12-2023 

s = input().strip()
dp = {}

def palindrome(st):
    return st==st[::-1]

def splits(st):
    if len(st)==1:
        return 0
        
    if st in dp:
        return dp[st]
        
    if palindrome(st):
        dp[st] = 0  
        return 0
        
    ans = len(st)
    for i in range(1, len(st)):
        if not palindrome(st[:i]):
            print(i)
            ans = min(ans, (splits(st[:i])+splits(st[i:]))+1)
    dp[st] = ans
    
    return dp[st]

ans = splits(s)

print(ans)