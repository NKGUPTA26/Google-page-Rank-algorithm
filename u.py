import numpy as np 
a=np.array([1,2,3,4,5,6])
sum=a.reshape(a.shape[:-2]+(-1)).sum(axis=-1)
print(sum)