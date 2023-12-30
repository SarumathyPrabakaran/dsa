
n = 7
c = 1
end = n*(n+1)

for i in range(n+1,0,-1):
    print(" "*(n+1-i), end="")
    for j in range(c, c+i-1):
        print(j,end=" ")
        c+=1
    for k in range(end-i+2,end+1, 1):
        print(k,end=" ")
    end = end-i+1
    print()