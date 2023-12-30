n = int(input())
l = list(map(int, input().split()))
k = int(input())
st = 0
i = 0
s = 0

while i<n:
    if s<k:
        s+=l[i]
        i+=1
    elif s==k:
        break
    else:
        s-=l[st]
        st+=1
if s==k:
    print("Yes")
else:
    print("No")


    










        