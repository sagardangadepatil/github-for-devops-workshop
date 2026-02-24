import numpy as np
#Aggrigate Function 
a = [1,2,3]
b = [1,2,4]
c = [2,2,3]
print("Value of First Array is :", a)
print("Value of Second Array is :", b)
print("Value of Third Array is :", c)
#Sum Function
print("Sum of first array is:", np.sum(a))
print("Sum of Second array is:", np.sum(b))
print("Sum of Third array is:", np.sum(c))
#Minimum value Function
print("Minimum value of First array is :", np.min(a))
print("Minimum value of Second array is :", np.min(b))
print("Minimum value of Third array is :", np.min(c))
#Median value Function
print("Median value of First array is :", np.median(a))
print("Median value of Second array is :", np.median(b))
print("Median value of Third array is :", np.median(c))
#Corelation Coefficient Function
print("Corelation coefficient value of First array is :", np.corrcoef(a))
print("Corelation coefficient value of Second array is :", np.corrcoef(b))
print("Corelation coefficient value of Third array is :", np.corrcoef(c))
#Standard Deviation Function
print("Standard Deviation value of First array is :", np.std(a))
print("Standard Deviation value of Second array is :", np.std(b))
print("Standard Deviation value of Third array is :", np.std(c))
