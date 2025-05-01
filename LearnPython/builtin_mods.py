import os
import datetime
current_directory  = os.getcwd()
print(current_directory)
print(datetime.datetime.now())
print("\n")

print(datetime.date.today())
print("\n")
print(datetime.datetime.today())
print("\n")


# check if a string begins with a specific char
# the startswith() function helps to check for strict string format
# It returns a boolean value 

message  = "Hi Valor"
print(message.startswith("Hi"))

#Check for the ending as well.
print("\n the ending")
print(message.endswith("or"))