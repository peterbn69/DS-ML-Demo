import numpy as np

arr = np.arange(25)
print(arr)
arr = arr.reshape(5, 5)
print(arr) # reshapes the array into a 5x5 matrix
print(arr.shape)

ranarr = np.random.randint(0, 50, 10)
print(ranarr)
print(ranarr.max())