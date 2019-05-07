import numpy as np

# one dim array

a1 = np.array([1, 2, 3, 4])
print(a1)
print('Dimension is: ', a1.ndim)
print('Size of array is: ', a1.size)
print('Data type: ', a1.dtype)
print('Size of an item: ', a1.itemsize)
a1 = np.array([1, 2, 3, 4], dtype=np.float64)
print('Now Size of an item: ', a1.itemsize)
print('Now array looks like: ', a1)
print('Shape of the array is: ', a1.shape)
mn1 = a1.min()
print('Minimum element is: ', mn1)
ma1 = a1.max()
print('Maximum element is: ', ma1)

# two dim array

a2 = np.array([[1, 2], [3, 4], [5, 6]])
print(a2)
print('Dimension is: ', a2.ndim)
print('Size of array is: ', a2.size)
print('Data type: ', a2.dtype)
print('Size of an item: ', a2.itemsize)
a2 = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64)
print('Now Size of an item: ', a2.itemsize)
print('Now array looks like: \n', a2)
print('Shape of the array is: ', a2.shape)
s = a2.reshape(2, 3)
print('After reshaping array is: \n', s)
mn2 = a2.min()
print('Minimum element is: ', mn2)
ma2 = a2.max()
print('Maximum element is: ', ma2)
sum1 = a2.sum()
print('Sum of Array is: ', sum1)
sum2 = a2.sum(axis=0)
sum3 = a2.sum(axis=1)
print("Axis level sum is: ", sum2)
print("Axis level sum is: ", sum3)

# Some properties

z = np.zeros((3, 4), dtype=int)  # print zeros
print('Array looks like: \n', z)

one = np.ones((3, 4), dtype=int)  # print ones
print('Array looks like: \n', one)

r1 = np.arange(1, 6)  # take range
r2 = np.arange(1, 10, 2)  # take range and steps
print('Array is: ', r1)
print('Array is: ', r2)

l = np.linspace(1, 5, 10)  # linearly spaced number between two number
print("Array is: \n", l)

sq = np.sqrt(a2)  # finding square root
print('Square root is: \n', sq)

sd = np.std(a2)  # finding standard deviation
print('Standard deviation is: ', sd)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print('Sum of two array is: \n', a + b)
print('Subtraction of two array is: \n', a - b)
print('Multiplication of two array is: \n', a * b)
print('Dot product of two array is: \n', a.dot(b))  # finding dot product

