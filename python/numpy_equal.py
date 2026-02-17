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

#Aggregate Function
print("1. Sum of First Array is : ", np.sum(arr1))  # Sum of array first Array 
print("2. Sum of Second Array is : ", np.sum(arr2))  # Sum of array Second Array 
print("3. Minimum Value of First Array is : ", np.min(arr1))
print("4. Minimum Value of Second Array is : ", np.min(arr2))
print("5. Mean Value of First Array is : ", np.mean(arr1))
print("6. Mean Value of Second Array is : ", np.mean(arr2))

print("7. Median Value of First Array is : ", np.median(arr1))
print("8. Median Value of Second Array is : ", np.median(arr2))

print("9. Coorelation Coefficient Value of First Array is : ", np.corrcoef(arr1))
print("10. Coorelation Coefficient Value of Second Array is : ", np.corrcoef(arr2))

print("11. Standard Deviation Value of First Array is : ", np.std(arr1))
print("12. Standard Deviation Value of Second Array is : ", np.std(arr2))

