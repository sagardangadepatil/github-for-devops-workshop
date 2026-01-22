
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

c = np.sum([[1,2], [5,6]], axis= 0)  # axis = 0 represent addition of arrays column wise i.e. vertically.
print("Addition of Array first number with first number of OTHER array and vice versa using axis =0 : ",c) 

c = np.sum([[1,2], [5,6]], axis= 1)  # axis = 1 represent addition of arrays row wise i.e. horizontally.
print("Addition of Array first number with second number of SAME array and vice versa using axis =1 : ",c) 

print("Enter dimentional array with single line :")

# Accept array elements from user separated by space
arr1 = input("Enter elements of the array separated by space: ").split()
arr2 = input("Enter elements of the array separated by space: ").split()
# Convert input strings to integers
arr1 = [int(x) for x in arr1]
arr2 = [int(y) for y in arr2]

# Print the array
print("The First array you entered is:", arr1)
print("The Second array you entered is:", arr2)
d = np.sum([arr1, arr2], axis =0)  # Addition of array like first number with first number of other array i.e. Column wise - Vertically.
print("Addition of array Vertically array wise:", d) 
d = np.sum([arr1, arr2], axis =1)  # Addition of array like first number with second number of same array i.e. Row wise - Horizontally.
print("Addition of array Horizontally array wise:", d) 
d = np.sum([arr1, arr2])  # Addition of array like first number with first number of other array
print("Addition of array with all in single digit :", d) 


# Sub-point2
import numpy as np
print("NumPy Array Mathematics : Subtract")
a,b = 10,20
c = np.subtract(a, b)
print("Example 1 - Subtraction of first and second number is :")
print(c)
print("Example 2 - Subtraction of a and b is :")
a = int(input("Type First Number :"))
b = int(input("Type Second Number :"))
print("First Number you entered is:", a)
print("Second Number you entered is:", b)
c = int(np.subtract(a,b))
print(c)
print("Subtraction of Second number from First Number is : ", c)

#c = np.subtract([1,2], [5,6], axis= 0)  # axis = 0 represent Subtraction of arrays column wise i.e. vertically.
print("Subtraction of Array first number with first number of OTHER array and vice versa using axis =0 : ",c) 

#c = np.subtract([[1,2], [5,6]], axis= 1)  # axis = 1 represent Subtraction of arrays row wise i.e. horizontally.
print("Subtraction of Array first number with second number of SAME array and vice versa using axis =1 : ",c) 

print("Enter dimentional array with single line :")

# Accept array elements from user separated by space
arr1 = input("Enter elements of the array separated by space: ").split()
arr2 = input("Enter elements of the array separated by space: ").split()
# Convert input strings to integers
arr1 = [int(x) for x in arr1]
arr2 = [int(y) for y in arr2]

# Print the array
print("The First array you entered is:", arr1)
print("The Second array you entered is:", arr2)
d = np.diff([arr1, arr2], axis =0)  # Subtraction of array like first number with first number of other array i.e. Column wise - Vertically.
print("Subtraction of array like first number with first number of other array :", d) 
d = np.diff([arr1, arr2], axis =1)  # Subtraction of array like first number with second number of same array i.e. Row wise - Horizontally.
print("Subtraction of array like first number with first number of other array :", d) 
d = np.diff([arr1, arr2])  # Subtraction of array like first number with first number of other array
print("Subtraction of array like first number with first number of other array :", d) 
