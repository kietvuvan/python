import random
lis=[]
n=int(input())
for i in range(n):
    randomlist=[random.randint(0,100) for i in range(15)]
    lis.append(randomlist)
print(lis)
