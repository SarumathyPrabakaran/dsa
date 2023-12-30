1



from collections import deque

m,n = map(int, input().strip().split())
l = [list(map(int, input().split())) for _ in range(m)]
q = deque()
tot = 0
for i in range(m):
    for j in range(n):
        if l[i][j]==2:
            q.append((i,j))
        if l[i][j]==1:
            tot+=1
c = 0   
days = 0
while(q):
    now_count = len(q)

    for _ in range(now_count):
        i,j = q.popleft()   # if pop(0) used, it is O(N). so time limit exceeds. so making it a deque. if not, use another newq and add the new values to that queue and putall the newq elements to oldque.
        
        diff = [(-1,0), (0,-1), (1,0), (0,1)]
        for g,h in diff:
            newi = i+g
            newj = j+h
            if(0<=newi<m and 0<=newj<n):
                if l[newi][newj]==1:
                    
                    l[newi][newj] = 2
                    q.append((newi,newj))
                    c+=1
    if tot==c:
        print(days+1)
        exit(0)

    days+=1
print(days) if tot==c else print(-1)