import string

n,k = map(int, input().strip().split(','))
l = []
for i in range(k):
    l.append(input().strip().split(','))
print(l)

all_letters = string.ascii_uppercase[:n]


ans = []


q = []
for char in all_letters:
    vis = {char}
    q = [char]
    while(q):
        now = q.pop(0)
        for ph in l:
            if now in ph:
                ind = ph.index(now)
                for suc in ph[ind+1:]:
                    if suc not in vis:
                        q.append(suc)
                        vis.add(suc)
    
    pre = [char]
    while(pre):
        now = pre.pop(0)
        for ph in l:
            if now in ph:
                ind = ph.index(now)
                for person in ph[:ind]:
                    if person not in vis:
                        pre.append(person)
                        vis.add(person)
    if(len(vis)!=n):
        ans.append(char)

print("N/A") if not ans else print(" ".join(ans))
                
            