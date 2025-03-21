import numpy as np
@np.vectorize
def f_to_cel(a):
    return (a-32)*5/9

arr = np.array([32, 68, 100, 212, 77])
print(f_to_cel(arr))