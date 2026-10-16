import numpy as np

print(np.arange(0, 10, 2)) # similar to range(0, 10, 2)

print(np.zeros(3))
print(np.zeros((2, 3))) # a 2x3 matrix of zeroes
print(np.ones(5))
print(np.ones((3, 2))) # a 3x2 matrix of ones

print(np.linspace(0, 10, 6)) # 6 numbers evenly spaced between 0 and 10
print(np.eye(3)) # a 3x3 identity matrix

print(np.random.rand(5)) # random numbers from 0 to 1
print(np.random.randn(2)) # random numbers from the standard normal distribution
print(np.random.randint(1, 100)) # a random number from 1 to 99
print(np.random.randint(1, 100, 10)) # 10 random numbers from 1 to 99