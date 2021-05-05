arr=[]
for i in range (1100,9090):
    if(i%11==0) and (i%3!=0):
        arr.append(str(i))
print(','.join(arr))