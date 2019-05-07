import numpy as np

a = np.array([1, 2, 3, 4])
print(a[0:3])  # Slicing elements in an array
print(a[:-1])  # [1 2 3]

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Array is: \n', b)

# different types of slicing techniques

print(b[0:2, 2])  # [3 6]
print(b[0])  # [1 2 3]
print(b[-1])  # [7 8 9]
print(b[-1, 1:3])  # [8 9]
print(b[:, 1:3])  # answer here(see down)
# [[2 3]
#  [5 6]
#  [8 9]]


for i in b.flat:
    print(i)  # it prints entire array in one dimension form

c = np.arange(6).reshape(3, 2)
d = np.arange(6, 12).reshape(3, 2)
print(c)
print(d)
v = np.vstack((c, d))  # print virtual stack
print(v)
h = np.hstack((c, d))  # print horizontal stack
print(h)

e = np.arange(30).reshape(2, 15)
print(e)
hs = np.hsplit(e, 3)  # horizontally split the array
print(hs)
vs = np.vsplit(e, 2)  # vertically split the array
print(vs)

p = e > 4
print(p)   # returns boolean value
print(e[p])  # returns elements in condition
e[p] = -1  # replace with -1
print(e)
