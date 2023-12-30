#Your code below
n = int(input().strip())
l = []
for i in range(n):
    l.append(input().strip())
d = {}
for i in l[0]:
    if i not in d:
        d[i] = 1

for i in range(1,n):
    for j in l[i]:
        if j in d and d[j]==(i):
            d[j]+=1
print(d)
for p,v in d.items():
    if(v==n):
        print(p,end="")


