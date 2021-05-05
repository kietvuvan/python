str=input()
num=''.join(filter(lambda x: x.isdigit(),str))
cha=''.join(filter(lambda x: x.isalpha(),str))

print(cha)
print(num)
temp=str.replace(cha, '')
temp=temp.replace(num,'')
print(temp)