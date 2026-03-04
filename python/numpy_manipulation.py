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

### #Concinate the arryas
print("Concatinate of First and Second Array is :", np.concatenate([arr1,arr2]))
### #Stack the arryas : Vertically
print("Stack the arryas : Vertically - First and Second Array is : \n", np.vstack([arr1,arr2]), '\n')
### #Stack the arryas row wise: Horizontally
print("Stack the arryas row wise: Horizontally - First and Second Array is : \n", np.hstack([arr1,arr2]), '\n')
### #Stack the arryas column wise
print("Stack the arryas column wise - First and Second Array is : \n", np.column_stack([arr1,arr2]), '\n')

x = np.arange(16).reshape(4,4) # Arranging 16 number ad reshaping with dimentions 
print("\n\n","Displaying array with 4x4 format for 16 numbers is :", x)
#Spliting the array
print("\n\n","Spliting the array from second position is: \n",np.hsplit(x,2), '\n', '\n') # Spliting the array from second position
print("\n\n","Spliting the array like first 3 columns in one array and remaining in next array :", np.hsplit(x,np.array([3])))

