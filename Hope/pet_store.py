n = int(input().strip())
ways = [0 for i in range(n+1)]
ways[1] = 1

for i in range(2,n+1):
    if i==2:
        ways[2] = 2
        continue
    ways[i] = 1*ways[i-1] + (i-1)*ways[i-2]

print(ways[-1])