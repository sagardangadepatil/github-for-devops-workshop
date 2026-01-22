
# Continuing NumPy
# Heading1
print("Mathemetical functions using NumPy:")
# Sub-point1
import numpy as np
print("NumPy Array Mathematics : Addition")
a,b = 10,20
c= np.sum([a,b])
print("Example 1 - Additon of 10 and 20 is :")
print(c)
print("Example 2 - Additon of a and b is :")
a = int(input("Type First Number :"))
b = int(input("Type Second Number :"))
print("First Number you entered is:", a)
print("Second Number you entered is:", b)
c = int(np.sum([a,b]))
print(c)
print("Addition of First Number and Second number is : ", c)

c = np.sum([[1,2], [5,6]], axis= 0)
print("Addition of Array first number with first number of OTHER array and vice versa using axis =0 : ",c) 

c = np.sum([[1,2], [5,6]], axis= 1)
print("Addition of Array first number with second number of SAME array and vice versa using axis =1 : ",c) 

print("Enter 1-dimentional array :")

# Accept array elements from user separated by space
arr1 = input("Enter elements of the array separated by space: ").split()
arr2 = input("Enter elements of the array separated by space: ").split()
# Convert input strings to integers
arr1 = [int(x) for x in arr1]
arr2 = [int(y) for y in arr2]

# Print the array
print("The First array you entered is:", arr1)
print("The Second array you entered is:", arr2)
d = np.sum([arr1, arr2])
print("Addition of array like first number with first number of other array :", d)
