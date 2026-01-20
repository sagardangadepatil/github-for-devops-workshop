#Numpy is an algebra operations in python
import numpy as np  #defining numpy as np as shortcut so we can use in future code
print("This is 1-dimensional array:")
a = np.array([1,2,3])    #this is 1-dimensional array 
print(a)
print("This is and 2-dimensional array:")
b = np.array([[1,2,3], [4,5,6]])     #This is and 2-dimensional array.
print(b)

#numpy array inspection:
#Checking Size of Array
c = np.array([[1,2,3], [4,5,6]])
print("Inspecting the Array : Checking size of Array")
print(c)
print("Size of Array:")
print(c.shape)  # Gives size of Array