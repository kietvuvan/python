from numpy import random
import numpy as np
arr=random.randint(1,11,size=100)
print(arr)
counts=np.bincount(arr)
print(counts)
print(np.argmax(counts))