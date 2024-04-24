s,k = input().strip().split()
k = int(k)
d = {}
n = len(s)
l,r = 0,0
ans = 0
for i in range(0, n):
    d[s[i]] = d.get(s[i],0)+1
    while len(d)>k and l<=i:
        m = d[s[l]]-1
        d[s[l]]-=1
        
        if m==0:
            del d[s[l]]
        l+=1
    if len(d)==k:
        ans = max(ans, i-l+1)
print(ans)


#Print String itself

s,k = input().strip().split()
k = int(k)
d = {}
l = 0
ans,st = 0, ''
for r in range(0, len(s)):
    d[s[r]] = d.get(s[r], 0)+1
    while len(d)>k:
        m = d[s[l]]-1
        d[s[l]]-=1
        if m==0:
            del d[s[l]]
        l+=1
    if len(d)==k:
        if ans<(r-l+1):
            st = s[l:r+1]
            ans = r-l+1
print(st)
