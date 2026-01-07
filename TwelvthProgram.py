############################# Adding and Removing in Numpy Arrays ################################

import numpy as np;

# Wap to perform append,insert in single dimension,insert in two dimension,delete in single dimension and delete in two dimension. 
print("=== Single-Dimensional Array Operations ===\n")

# Create a 1D array
arr1d = np.array([10, 20, 30, 40, 50])
print("Original 1D array:")
print(arr1d)

# 1. Append elements to 1D array
appended_1d = np.append(arr1d, [60, 70])
print("\nAfter appending [60, 70]: ",appended_1d)


# 2. Insert elements in 1D array (at index 2, insert 25 and 35)
inserted_1d = np.insert(arr1d, 2, [25, 35])
print("\nAfter inserting [25, 35] at index 2: ",inserted_1d)

# 3. Delete elements from 1D array (delete element at index 1 and 3)
deleted_1d = np.delete(arr1d, [1, 3])
print("\nAfter deleting elements at indices 1 and 3: ",deleted_1d)

print("\n\n=== Two-Dimensional Array Operations ===\n")

# Create a 2D array (3x4)
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
print("Original 2D array:")
print(arr2d)

# 1. Append to 2D array

# AXIS 0 -> Row
# AXIS 1 -> Column

new_row = np.array([[13, 14, 15, 16]])
appended_2d_row = np.append(arr2d, new_row, axis=0)
print("\nAfter appending a new row:")
print(appended_2d_row)

new_col = np.array([[100], [200], [300]])
appended_2d_col = np.append(arr2d, new_col, axis=1)
print("\nAfter appending a new column:")
print(appended_2d_col)

# 2. Insert in 2D array
insert_row = np.array([[99, 99, 99, 99]])
inserted_2d_row = np.insert(arr2d, 1, insert_row, axis=0)
print("\nAfter inserting a row at index 1:")
print(inserted_2d_row)

insert_col = np.array([[50], [60], [70]])
inserted_2d_col = np.insert(arr2d, 2, insert_col, axis=1)
print("\nAfter inserting a column at index 2:")
print(inserted_2d_col)

# 3. Delete from 2D array
deleted_2d_row = np.delete(arr2d, 1, axis=0)
print("\nAfter deleting row at index 1:")
print(deleted_2d_row)

deleted_2d_col = np.delete(arr2d, 2, axis=1)
print("\nAfter deleting column at index 2:")
print(deleted_2d_col)