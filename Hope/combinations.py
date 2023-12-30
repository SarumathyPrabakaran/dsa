from itertools import combinations


def solve(s):
    n = len(s)
    for i in range(1,2**n):
        for j in range(n-1,-1,-1):
            if(i&(1<<j)):
                print(s[n-j-1],end= "")
        print()
    

def solve_itertools(s):
    for i in range(1,len(s)+1):

        for c in (combinations(s,r=i)):
            print(c)

solve("abc")
print("------------")
solve_itertools("abc")