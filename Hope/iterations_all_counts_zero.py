#Your code below
row,col = map(int, input().strip().split())
l = [list(map(int, input().split())) for _ in range(row)]
k = int(input().strip())

c = 0

for i in range(row):
    for j in range(col):
        if l[i][j]!=0:
            c+=1
# print(c)

def dfs(i,j):
    global c
    c = c-1 if not l[i][j]==0 else c
    l[i][j] = 0
    
    for dx,dy in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
        if 0<=dx<row and 0<=dy<col and l[dx][dy]!=0:
            c-=1
            # l[dx][dy] = 0
            dfs(dx,dy)
            
ans = 0
for i in range(0, row):
    for  j in range(0, col):
        if l[i][j]==k:
            ans+=1
            dfs(i,j)
            

print(ans) 