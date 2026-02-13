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

print("Comparisum of Array is [Element wise] : ")
d = np.equal(arr1, arr2)  # Comparisum of array Element wise
print("Comparisum of array like first number with first number of other array :", d)

print("Comparisum of Array is [Array wise] :")
d = np.array_equal(arr1, arr2)  # Comparisum of array Array wise
print("Comparisum of first array with other array :", d)
