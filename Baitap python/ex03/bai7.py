filename='bai6.txt'
f=open(filename,encoding='utf-8')
lines=f.read()

#print(lines)
str=",.!;/:-\+"
for i in str:
    lines=lines.replace(i,"")
lines=lines.lower()
lines=lines.split()
d={}
for word in lines:
    d[word]=d.get(word,0)+1

print(d)