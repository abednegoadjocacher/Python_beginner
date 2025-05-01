try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"{number} divide by 10 is {result}")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Number can not be Zero")