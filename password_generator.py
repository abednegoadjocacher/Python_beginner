import random
# Password generator
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['~','!','@','#','$','%','^','&','*','(',')','-','+','_']
numbers=['1','2','3','4','5','6','7','8','9','0']
random.shuffle(letters)
N_letter=int(input("How many letters should be in your password: "))
N_symbol=int(input("How many symbols should be in your password: "))
N_number=int(input("How many numbers should be in your password: "))
password=[]
for i in range(1,N_letter+1):
    characters=random.choice(letters)
    password+=characters
#print(password)
for i in range(1,N_symbol+1):
    Sym=random.choice(symbols)
    password+=Sym
#print(password)
for i in range(1,N_number+1):
    num=random.choice(numbers)
    password+=num
random.shuffle(password)
#print(password)
Passwd=""
for i in password:
    Passwd+=i
print(Passwd)




# This will generate Easy password in orderly manner
#letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#symbols=['~','!','@','#','$','%','^','&','*','(',')','-','+','_']
#numbers=['1','2','3','4','5','6','7','8','9','0']
#random.shuffle(letters)
#N_letter=int(input("How many letters should be in your password: "))
#N_symbol=int(input("How many symbols should be in your password: "))
#N_number=int(input("How many numbers should be in your password: "))
#password=""
#for i in range(0,N_letter+1):
#    characters=random.choice(letters)
#    password+=characters
#print(password)
#for i in range(0,N_symbol+1):
#    Sym=random.choice(symbols)
#    password+=Sym
#print(password)
#for i in range(0,N_number+1):
#    num=random.choice(numbers)
#    password+=num
#print(password)