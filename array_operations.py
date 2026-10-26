#Create 1-D array of 10 integers

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Number of Dimensions:", arr.ndim)

#Arithmetic operations on two NumPy arrays

import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Array A:", a)
print("Array B:", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

#Maximum, minimum, sum and average

import numpy as np

arr = np.array([10, 25, 15, 40, 5, 30, 50, 20, 35, 45])

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


#Separate even and odd numbers using Boolean indexing

import numpy as np

arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Array:", arr)
print("Even numbers:", even)
print("Odd numbers:", odd)

#Reshape array from 1 to 12

import numpy as np

arr = np.arange(1, 13)

print("Original Array:")
print(arr)

matrix1 = arr.reshape(2, 6)
matrix2 = arr.reshape(3, 4)
matrix3 = arr.reshape(4, 3)

print("\n2 x 6 Matrix:")
print(matrix1)

print("\n3 x 4 Matrix:")
print(matrix2)

print("\n4 x 3 Matrix:")
print(matrix3)

#Matrix addition of two 3 × 3 matrices

import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

result = a + b

print("Matrix A:")
print(a)

print("\nMatrix B:")
print(b)

print("\nMatrix Addition:")
print(result)

#Matrix multiplication using NumPy

import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

result = np.matmul(a, b)

print("Matrix A:")
print(a)

print("\nMatrix B:")
print(b)

print("\nMatrix Multiplication:")
print(result)

#Transpose of a 3 × 4 matrix

import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Original Matrix:")
print(matrix)

print("\nTranspose:")
print(matrix.T)

#Operations on a 4 × 4 matrix

import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Matrix:")
print(matrix)

print("\nFirst Row:")
print(matrix[0])

print("\nLast Column:")
print(matrix[:, -1])

print("\nDiagonal Elements:")
print(np.diag(matrix))

print("\nSecond and Third Rows:")
print(matrix[1:3])

#Sum of each row and each column

import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

row_sum = np.sum(matrix, axis=1)
column_sum = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)

print("\nSum of each row:")
print(row_sum)

print("\nSum of each column:")
print(column_sum)