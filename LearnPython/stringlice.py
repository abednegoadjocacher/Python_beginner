course = "Python is my favorite programming language"
#         0123 ------------------------------------42   

# String slice
print(course[0:]) #This prints the entire string.
print(course[1:10])
print(len(course)) #This print the length of the string.
print(course[1:-1]) #this print the string excluding the first character and the last one.



#Square of numbers in a list
square = [x**2 for x in range(1,8)]
print(square)



#Dictionary creation
print("\nDictionary")
student = {
    "name": "Abednego",
    "age": 900,
    "course": "BSC. Computer Science"
}

print(student)
print(student.keys()) #print only the keys
print(student.values()) # this print the values
print(student.items()) #this print both keys and values

#String manipulation
print("\n")
text = "   hello abednego!   "
print(text.count("e")) #This count the occurrence of "e"
print(text.strip()) #removes excess whitespace at both ends when necessary
print(text.capitalize())