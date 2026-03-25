# AIM: To understand and work with different data structures such as arrays, lists, data frames, and matrices in Python. [cite: 61, 62]
# DESCRIPTION: Data structures are used to store and organize data efficiently. [cite: 63, 64]
# Lists are mutable and store heterogeneous data. Arrays (NumPy) store homogeneous numerical data. [cite: 66, 67]
# DataFrames (pandas) store tabular data. Matrices are 2D numerical structures for math. [cite: 68, 69]

import numpy as np [cite: 72]
import pandas as pd [cite: 73]
# 1. List
marks = [85, 90, 78, 88] [cite: 75]
print("List of Marks:", marks) [cite: 76]
# 2. Array
arr = np.array([1, 2, 3, 4, 5]) [cite: 79]
print("\nArray Elements:", arr) [cite: 80]
# 3. DataFrame
data = {'Name': ['Ram', 'Sita', 'Ravi'], 'Marks': [85, 92, 78]} [cite: 82, 87]
df = pd.DataFrame(data) [cite: 88]
print("\nDataFrame:\n", df) [cite: 88]
# 4. Matrix
matrix = np.array([[1, 2], [3, 4]]) [cite: 90, 91]
print("\nMatrix:\n", matrix) [cite: 90]
