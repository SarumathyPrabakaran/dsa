row,col = map(int, input().strip().split())
mat = [ list(map(int, input().strip().split())) for _ in range(row)]

l = []
r = row-1
c = 0
cp = 0
rp = 0
for s in range(0, row+col):
    if c>=row:
            c = cp+1
            cp = cp+1
    else:
            c = 0
    r = s - c
    l = []
    while(0<=r<row and 0<=c<col):
        if not s&1:
            print(mat[r][c], end=" ")
        else:
            l.append(mat[r][c])
        r-=1
        c+=1
        
    print(*l[::-1])
                