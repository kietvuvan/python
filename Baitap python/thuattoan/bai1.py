
n=int(input())
l=[]
x=[0]*n
def tri(i):
    for j in range(2):
            x[i]=j
                     
            if i==n-1:
                print(x)
                
            else:
                tri(i+1)
tri(0)
