import numpy as np

a = np.arange(12).reshape(3, 4)
print('This is Fortran order')
for i in np.nditer(a, order='F'):  # fortran order
    print(i)
print('This is C order')
for i in np.nditer(a, order='C'):  # c order
    print(i)
