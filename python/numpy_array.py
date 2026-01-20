# Heading1

print("Numpy is an algebra operations in python")

import numpy as np  #defining numpy as np as shortcut so we can use in future code
# Sub-point
print("This is 1-dimensional array:")
a = np.array([1,2,3])    #this is 1-dimensional array 
print(a)


print("This is and 2-dimensional array:")
b = np.array([[1,2,3], [4,5,6]])     #This is and 2-dimensional array.
print(b)

# Heading2
print("NumPy Array Inspection:")
print("Type-1 : Checking Size of Array")
# Example-1
c = np.array([[1,2,3], [4,5,6]])

print("Example-1")
print(c)
#.shape - Returns a tuple consisting of array dimentions. Can also be used to resize the array.

print("Size of Array Example-1:")
print(c.shape)  # Gives size of Array

print("Example-2")
d =np.array([[1,2,3,4],[5,6,7,8],[0,9,0,0]])
print(d)
print("Size of Array Example-2:")
print(d.shape)

print("Type-2 : Resize of Array - using '.shape'")
print("Resizing the Array - ([1,2,3]) in to 3x1 format")
a.shape = (3,1)
print(a)
print("Resizing the Array - ([[1,2,3], [4,5,6]]) in to 2x3 format")
b.shape = (2,3)
print(b)
print("Resizing the Array - ([[1,2,3,4],[5,6,7,8],[0,9,0,0]]) in to 4x3 format")
d.shape = (4,3)     ##Trick is  x*y = Total number of elements in the array
print(d) 

print("Type-3 : Return the dimention of Array - using '.ndim'")
e = np.arange(24)
print("Values of 24 from 0 using .arange")
print(e)
print("Shows the dimention using .ndim :")
print(e.ndim)
print("Shows number using np.arange :(start, stop)")
f = np.arange(0, 25)
print(f)
print(f.ndim)
print("Reshape our array - np.arange(24)")
g = e.reshape(2,3,4) # Trick: calculate factor of 24 i.e. 1,2,3,4,6,12,24
print(g)
print("The Dimention of array using np.ndim :")
print(g.ndim)
print("Find the number of elements in the array - use np.size function")
print(g.size)

print("Find the number of elements in the array - use np.size function for array ([[1,2,3,4],[5,6,7,8],[0,9,0,0]]):")
print(d.size)

print("Type-4 : Find the datatype of Array - using 'np.dtype'")
h = np.arange(24)
print("print the datatype of 24 i.e. np.arange(24) is :")
print(h.dtype)
h = np.arange(24, dtype=float)
print("print the datatype of 24 i.e. np.arange(24, dtype=float) is :")
print(h.dtype)