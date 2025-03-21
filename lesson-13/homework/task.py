import numpy as np

#1

arr = np.arange(10, 49)

#2

arr2 = np.arange(9).reshape((3, 3))

#3

arr3 = np.eye(3, dtype=int)

#4

arr4 = np.random.rand(3, 3, 3)

#5

arr5 = np.random.randint(0, 100, size=(10, 10))

print(f"MIN: {np.min(arr5)}")
print(f"MAX: {np.max(arr5)}")

#6

arr6 = np.random.randint(0, 1000, size=30)
print(f"Mean: {np.mean(arr6)}")

#7

arr7 = np.random.randint(0, 100, size=(5, 5))
min = np.min(arr7)
max = np.max(arr7)
norm = (arr7 - min) / (max - min)
print(f"Normalized: {norm}")

#8

a8 = np.random.randint(0, 100, size=(5, 3))
b8 = np.random.randint(0, 100, size=(3, 2))

print(f"Product: {np.dot(a8, b8)}")

#9

a9 = np.random.randint(0, 100, size=(3, 3))
b9 = np.random.randint(0, 100, size=(3, 3))
print(f"Product: {np.dot(a9, b9)}")

#10

arr10 = np.random.randint(0, 10, size=(4, 4))
print(f"Transposed: {np.transpose(arr10)}")

#11

arr11 = np.random.randint(0, 10, size=(3, 3))
print(f"Determinant: {np.linalg.det(arr11)}")

#12

a12 = np.random.randint(0, 100, size=(3, 4))
b12 = np.random.randint(0, 100, size=(4, 3))

print(f"Product: {np.dot(a12, b12)}")

#13

a13 = np.random.randint(0, 100, size=(3, 3))
b13 = np.random.randint(0, 100, size=(3, 1))

print(f"Product: {np.dot(a13, b13)}")

#14

print(f"Solution: {np.linalg.solve(a13, b13)}")

#15

arr15 = np.random.randint(0, 100, size=(5, 5))

print(f"Row sum: {np.sum(arr15, axis=1)}")
print(f"Column sum: {np.sum(arr15, axis=0)}")
