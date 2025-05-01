'''
A simple log in page for user
The must enter name and password validation
'''
print("Create account")
username = input("Enter user name: ")
password = input("Enter user password: ")
print("Account created successfully!\nLog in Now")
username_1 =input("Enter user name: ")
password_1 = input("Enter password: ")
# Check if user name and password  is correct
if username_1==username and password_1==password:
    print("Log in successfully")
else:
    print("Access denial")

