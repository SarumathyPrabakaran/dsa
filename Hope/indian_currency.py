
denominations = [1,2,5,10,20,50,100,200,500,2000]

# denominations = [1,7,10]

denominations = sorted(denominations, reverse=True)

c = 0
amount = 15

for deno in denominations:
    if deno<=amount:
        c+= (amount//deno)
        amount = amount%deno


print(c) if amount==0 else print(-1)


