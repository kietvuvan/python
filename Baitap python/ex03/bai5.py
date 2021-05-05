from operator import itemgetter
lis=[]
names=[]
while True:
    str=input().strip()
    if not str:
        break
    lis.append(tuple(str.split(',')))

lis.sort(key=itemgetter(1),reverse=False) # sort score
print(lis)

for i in range(len(lis)):
    names.append(lis[i][0])
print(sorted(names,key=lambda x: x.split()[-1:]))# sort name
