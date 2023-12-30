n = int(input())
st = []
end = []

def convert(s):
    hr,min = s.split(':')
    return hr*60+min


for _ in range(n):
    p,q = map(convert, input().split())
    st.append(p)
    end.append(q)

comp, maxc = 0,0
i,j = 0,0

while(i<n and j<n):
    if st[i]<end[j]:
        comp+=1
        i+=1
    elif(st[i]>end[j]):
        comp-=1
        i-=1
    else:
        i+=1
        j+=1
    maxc = max(maxc, comp)

print(comp)

