import numpy as np

n1 = np.array([1, 2, 3, 4, 5, 6])
n2 = np.array([6, 7, 8, 9, 10, 11])
n3 = np.array([[11, 12, 13], [14, 15, 16]])
n4 = np.array([[21, 22, 23], [24, 25, 26]])

print("n1:")
print(n1)
print("\n")

print("n2:")
print(n2)
print("\n")

#2D array
print("n3:")
print(n3)
print("\n")

#Dimension of an array
print("Dimension of array n3:")
print(n3.ndim)
print("\n")

#Filling an array with zeroes
print("Filling with zeroes:")
z1 = np.zeros((2,2))
print(z1)
print("\n")

#Negative indexing
print("Negative indexing of n1:")
print(n1[-1])
print("\n")

#Array Slicing
print("Slicing array of n2:")
print(n2[2:4])
print("\n")

#Shape of array
print("Shape of array:")
print(n3.shape)
print("\n")

#Reshaping array
print("Reshaping n1:")
print(n1.reshape(2, 3))
print("\n")

#Concatenating array
print("Concatenation of n1 and n2:")
result = np.concatenate((n1, n2))
print(result)
print("\n")

#Splitting of an array
print("Array splitting of n2:")
sp = np.array_split(n2, 2)
print(sp[0])
print(sp[1])
print("\n")

#Searching of an array
print("Index of 6 in n1:")
index = np.where(n1==6)
print(index)
print("\n")

#Sorting
sentence = np.array(["I", "Am", "Kundana", "Mani", "B"])
print("Original array:")
print(sentence)
print("Sorted array:")
print(np.sort(sentence))
print("\n")

#Arithmetic operations:
print("Sum of n3 and n4 (rows):")
print(np.sum([n3, n4]), axis = 1)
print("Sum of n3 and n4 (columns):")
print(np.sum([n3, n4]), axis = 0)
print("\n")
print("Sum of n1 and n2:")
print(np.sum([n1, n2]))
print("\n")
print("Multiplication of n1 and n2:")
print(np.multiply(n1, n2))
print("\n")
print("Division of n1 and n2:")
print(np.divide(n1, n2))
print("\n")