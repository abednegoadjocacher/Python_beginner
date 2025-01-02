markOfStudents=[50,32,13,56,0,-9,-7,-1,46,78,90,11] #This is List
markOfStudents.append(45) #To add a single number to the list
markOfStudents.extend([2,3]) #To add multiple numbers
print(markOfStudents) #To print the list
print(markOfStudents[:7:2])
print(markOfStudents[3]) #To print a specific mark
print("The length of the list :",len(markOfStudents))
markOfStudents.sort()
print("Sorted result:",markOfStudents)
markOfStudents.reverse()
print("The reversed order:",markOfStudents)