n=int(input())

def tri_Pascal(n):
     result=[1]
     temp=[0]
     for _ in range(n):
         print(result)
         result=[x+y for x,y in zip(result+temp,temp+result)]
tri_Pascal(n)   


