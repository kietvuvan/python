s_bin=input().split(',')
lis=[]
print(s_bin)

for i in (s_bin):
    x=int(i,2)
    if  not x%5==0:
        lis.append(i)
print(','.join(lis))


