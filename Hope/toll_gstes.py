#Your code below
n,d = map(int, input().strip().split())
k = int(input())
dist = list(map(int, input().strip().split()))
fee = list(map(int, input().strip().split()))

dp = [0 for _ in range(0, k+1)]
 
dp[0] = 0
dp[1] = fee[0]
 
ans = dp[1]
 
for i in range(2, k+1):
    p = i-1
    prev = dist[i-1]-d-1
    while(dist[p]>prev and p>=-1 and prev>=0):
        p-=1
    
    val = dp[p+1]
    dp[i] = max(dp[i-1], val+fee[i-1])
    ans = max(ans, dp[i])

print(dp)
print(ans)