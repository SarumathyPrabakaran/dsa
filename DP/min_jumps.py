from functools import cache
arr = [3,4,2,1,2,3,7,1,1,1,2,5]




def min_jumps(n,  curr, dp):
    if curr==n-1:
        return 0
    if curr>=n:
        return float("inf")
    
    if dp[curr]!=-1:
        return dp[curr]
    
    ans = float("inf")
    jumps = arr[curr]

    for j in range(1, jumps+1):
        subproblem = min_jumps(n, curr+j, dp)
        
        if subproblem!=float("inf"):
            ans = min(ans, subproblem+1)
    dp[curr] = ans
    print(curr+j, ans)
    return ans


def min_jumpsBU(n):
    dp = [-1 for _ in range(n+1)]

    dp[0] = 0
    dp[1] = 1 if arr[0]>=1 else 0
    # for i in range(2,n+1):
    #     dp[i] =  

print(min_jumps(len(arr), 0, [-1 for i in range(len(arr)+1)]))



