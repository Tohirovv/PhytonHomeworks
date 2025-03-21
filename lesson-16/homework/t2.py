import numpy as np
@np.vectorize
def n_power(a, b):
    return a**b

a = np.array([2, 3, 4, 5])
b = np.array([1, 2, 3, 4])

print(n_power(a, b))