import numpy as np 
arr_one=np.ones((3,3),dtype=float)
print(arr_one)
arr=np.pad(arr_one,pad_width=1,mode="constant",constant_values=0)
print(arr)