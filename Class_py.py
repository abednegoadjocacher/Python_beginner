class TeacherDetails: # Class
    def __init__(self, teacher_name,teacher_address):
        self.Name=teacher_name
        self.Address=teacher_address
    def display(self,subject):
        print(f"Sir {self.Name} is your {subject} teacher")
    
#Derived class that inherit parent class
class AssistantTeacher(TeacherDetails):
    def salary(self):
        print("TA's are not paid!")


at_1 = AssistantTeacher()
print(at_1.Name())

first_teacher = TeacherDetails("Abednego", "Accra-NIC")#Create an object of the class
second_teacher = TeacherDetails("Emily","Tema")


print(second_teacher.Name)
print(first_teacher.Name)
print(first_teacher.display("Python"))