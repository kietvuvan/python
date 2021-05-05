from collections import Counter

filename='bai5.txt'
f=open(filename,encoding='utf-8')
lines=f.read()

#print(lines)
str=",.!;/:-\+"
for i in str:
    lines=lines.replace(i,"")
lines=lines.lower()
lines=lines.split()
#print(lines)
count=Counter(lines)
print(count.most_common(1))
print(type(count))