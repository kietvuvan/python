names=input().split(',')
print(sorted(names,key=lambda x: x.split()[-1:]))
