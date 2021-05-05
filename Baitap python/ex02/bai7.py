m=int(input('input row:'))
n=int(input('input col:'))
#matrix=[[0 for i in range(0,m)] for i in range(0,n)]
arr1=[[0 for i in range(0,m)] for i in range(0,n)]
arr2=[[0 for i in range(0,m)] for i in range(0,n)]
def input_matrix(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            arr[i][j]=int(input('arr['+str(i)+']['+str(j)+']='))

def add_matrix(arr1,arr2):
    result = [list(map(sum, zip(*t))) for t in zip(arr1, arr2)]
    return result

def mul_arr(arr1,arr2):
    result=[[sum(a*b for a,b in zip(arr1_row,arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]
    return result
   
def output_matrix(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            print(arr[i][j],end=' ')

input_matrix(arr1)
input_matrix(arr2)
print(add_matrix(arr1,arr2))
print(mul_arr(arr1,arr2))