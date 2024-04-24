grid = [[0,6,0],[5,8,7],[0,9,0]]
r,c = len(grid), len(grid[0])

dp = [[0 for i in range(0, c)] for j in range(0, r)]

for i in range(0, r):
    for j in range(0, c):
        dp[i][j] = max(dp[i-1][j] if i>0 else 0, dp[i][j-1] if j>0 else 0)
    dp[i][j] += grid[i][j]
print(dp)