import numpy as np
a = np.array([[1,3,5,7,9],
     [1,1,4,5,8],
     [2,4,6,7,9]])
print(a[-1, :])
print(a[:, -1])
b = np.transpose(a)
print(b)
print(b[-1,:])