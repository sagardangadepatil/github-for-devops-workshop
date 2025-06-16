#List are group of values within square bracket []
myList = ['a', 10, 95.95, 'Jhon']
print(myList)
myList+=["Cina"]
#Concatenate operation on myList and line no 4
print("Concatinate List values as ", myList)
myList2 = ["Measurement of Wrestlers", "group", "hight", 'weight', "Name", '=']
print("Displaying new List is ", myList2)
myList2+=myList
print(myList2)
#Repeat Function in List
Repeat_string_myList3 = myList * 2
print("Repeat function for myList is : ", Repeat_string_myList3)
#Slice Function in List
myList4 = print("Slice last 5 objects from myLists2 is ", myList2[1:5])
#Append Function in List
print(myList)
myList5 = "End of Wrestlers Details"
myList.append(myList5)
print(myList)  #Append myList5 into myList
#Insert Function
myList.insert( 0, "Group")
myList.insert(2, "Hight")
myList.insert(4, "Weight")
myList.insert(6, "Name")
print(myList)
