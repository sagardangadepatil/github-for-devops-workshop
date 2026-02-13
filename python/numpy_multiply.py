# Sub-point2
import numpy as np
# Accept array elements from user separated by space
arr1 = input("Enter elements of the array separated by space: ").split()
arr2 = input("Enter elements of the array separated by space: ").split()
# Convert input strings to integers
arr1 = [int(x) for x in arr1]
arr2 = [int(y) for y in arr2]

# Print the array
print("The First array you entered is:", arr1)
print("The Second array you entered is:", arr2)

d = np.multiply(arr1, arr2)  # Multiply of array
print("Multiply of array like first number with first number of other array :", d)

d = np.prod([arr1, arr2], axis =0)  # Subtraction of array like first number with first number of other array i.e. Column wise - Vertically.
print("Multiply of array like first number with first number of other array :", d) 
d = np.prod([arr1, arr2], axis =1)  # Subtraction of array like first number with second number of same array i.e. Row wise - Horizontally.
print("Subtraction of array like first number with first number of other array :", d) 
d = np.prod([arr1, arr2])  # Subtraction of array like first number with first number of other array
print("Subtraction of array like first number with first number of other array :", d) 
