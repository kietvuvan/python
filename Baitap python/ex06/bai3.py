
s=input().split(' ')
print(s)
print(len(s))
dic={}
for i in range(len(s)):
    dic[s[i]]=s[i]+''.join(reversed(s[i]))
print(dic)
