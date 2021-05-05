import filecmp
file1=open("file1.txt",'r') 
file2=open("file2.txt",'r') 
compare=filecmp.cmp(file1,file2)
print(compare)