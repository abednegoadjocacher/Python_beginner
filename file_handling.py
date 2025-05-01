count_file=open("all_text.txt", "r")
print(count_file.readable()) # Check if the file is readable. It returns true if readable. Else otherwise
print(count_file.readline())# Reads the file content by single line only
#print(count_file.readlines())# Reads the entire file and print it out as list

for file in count_file.readlines():# To read the file line by line using for loop
    print(file)
count_file.close()