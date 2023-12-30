

#top down

def top_down(n, k):
    dp = [0 for i in range(n+1)]


    def helper(n,k, dp):
        if n<0:
            return 0
        if n==0 or n==1:
            dp[n] = 1
            return  1

        if dp[n]!=0:
            return dp[n]
        

# dp[n] = dp[n-1] + dp[n-2] + dp[n-3] +....+ dp[n-k]
        for j in range(1, k+1):
            dp[n]+= helper(n-j, k, dp)
        return dp[n]
    
    return dp, helper(n,k, dp)


def bottom_up(n, k):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        for j in range(i-k, i):
            dp[i] += dp[j]
    
    return dp, dp[n]

def sliding(n,k):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = 2*dp[i-1] - dp[i-(k+1)]
    
    return dp, dp[n]




n = 5
k = 3

ans1 = top_down(n,k)
ans2 = bottom_up(n,k)

ans3 = sliding(n,k)

print("TOP DOWN: ",ans1)
print("BOTTOM UO: ",ans2)
print("TSLIDING: ",ans3)





        

    
