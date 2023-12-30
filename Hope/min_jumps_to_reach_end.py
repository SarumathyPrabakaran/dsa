
n = int(input().strip())
l = list(map(int, input().strip().split()))

jumps = 1
mri = l[0]
steps = l[0]

for i in range(1, len(l)-1):
    steps-=1
    mri = max(mri, i+l[i])

    if steps==0:
        jumps+=1
        steps = mri-i
    

# Only one element -  return 0  
print(jumps if n>1 else 0)
