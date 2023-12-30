
n = int(input().strip())
l = list(map(int, input().strip().split()))
swaps = 0
cycle = []

p = set()
i = 0


#detect cycle 
while(i<n):
        if not l[i]:
            i+=1
            continue
        if i+1!=l[i]:
            p.add(i+1)
            i = l[i]-1
            if i+1 in p:
                cycle.append(p)
                for j in p:
                    l[j-1] = None
                p = set()
                i+=1
        else:
            i+=1
                

#add edges-1
for c in cycle:
    swaps += len(c)-1
    
print(swaps)
        



## Descending:
n = int(input().strip())
l = list(map(int, input().strip().split()))

cyc = []
swaps = 0
p = set()
i = 0
while(i<n):
    if n-i!=l[i]:
        p.add(n-i)
        i = n-l[i]
        if n-i in p:
            print(cyc)
            cyc.append(p)
            p = set()
            i+=1
    else:
        i+=1

print(cyc)


for c in cyc:
    swaps += len(c)-1
    
print(swaps)