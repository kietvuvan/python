n=int(input())
dic={}
reverse=""
for i in range(1,n+1):
    dic[i]=i*i
    dic[i]=int(str(dic[i])[::-1])
    
print(dic)