import numpy as np

# Create random NumPy array
arr = np.random.randint(1, 100, 10)

# Calculate statistics
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)

print("Array:", arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
