n=int(input())
m=int(input('length of list'))
import random 
from collections import Counter
li=[random.randint(0,n) for i in range(m)]
print(li)
print(max(li))
print(min(li))
c=Counter(li)
print(c.most_common(1))
