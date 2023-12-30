

def lis(s):
    n = len(s)
    length = 1
    dp = [1 for i in range(n)]

    for i in range(1, n):
        for j in range(0,i):
            if s[j]<s[i]:
                dp[i] = dp[j]+1
                length = max(length, dp[i])
    print(dp)
    return length


print(lis([10,20,40,50,45,51,56,78,99]))