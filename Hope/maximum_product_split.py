

n = int(input().strip())
if n<=3:
    print(n-1)
    exit(0)


threepow = n//3
curr = 3**threepow

if(n%3==1):
    curr//=3
    curr*=4
if(n%3==2):
    curr*=2

print(curr)