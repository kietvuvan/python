import numpy as np 
from numpy import random
arr=random.randint(-10,10,size=(5,6))
print(arr)
arr=arr.clip(min=0)
print(arr)