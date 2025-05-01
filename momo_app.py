class MomoApp:
        # The __init__(self) function help you to pass the values of the objects created from the class.
        def __init__(self,Fname,Lname,D_of_birth,PIN):
            self.fname = Fname
            self.lname=Lname
            self.dateOfBirth=D_of_birth
            self.pin= PIN
        # A method to create user account.
        def createAccount(self):
              F_name=input("Enter first name: ")
              L_name=input("Enter last name: ")
              Gh_ID=input("Ghana Card ID: ")
              phone_Number=input("Enter phone number: ")
              passWord=input("Create your new PIN: ")
              print(f"Thank you.\nYour account has been created successfully.\nPlease do not  share your PIN with anybody.")
            
        
# user_1 = MomoApp("Abed","Adjo","12/12/2022","3456")
# print(user_1.fname)
# user_2 = MomoApp()
# user_2.createAccount()