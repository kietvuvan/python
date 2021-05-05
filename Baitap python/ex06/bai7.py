
sum = 0
while True:
    s = input("")
    if not s:
        break
    values = s.split(" ")
    enter = values[0]
    amount = int(values[1])
    if enter=="D":
        sum+=amount
    elif enter=="W":
        sum-=amount
    else:
        pass
print (sum)