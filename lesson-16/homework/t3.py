import numpy as np
a = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])

y = np.array([7, 4, 5])
print(np.linalg.solve(a, y))