class Stack:
    def __init__(self):
        self.stack_list=[]

    def push(self, element):
        self.stack_list.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack_list.pop()

        else:
            print("Empty stack")

    def is_empty(self):
        return len(self.stack_list)==0
    
    def size(self):
        return len(self.stack_list)
    
    def peep(self):
        return self.stack_list[-1]
    
    def clear(self):
        return self.stack_list.clear()
    try:
        def delete(self):
            return self.delete()
    except:
        print("Stack does not exist")
    def display(self):
        return self.stack_list[::-1]

    def search(self, element):
        if element in self.stack_list:
            return len(self.stack_list) - self.stack_list.index(element)  # 1-based index from top
        return "Search not found!"

stack = Stack()

while True:
    print("\n1. Enter an element into the stack")
    print("2. Pop an element from the stack")
    print("3. Peek at the top element")
    print("4. Display stack contents")
    print("6. Search stack contents")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        element = input("Enter the element to push into the stack: ")
        stack.push(element)
        print(f"'{element}' has been added to the stack.")
    elif choice == "2":
        try:
            removed = stack.pop()
            print(f"Removed element: {removed}")
        except IndexError as e:
            print(e)
    elif choice == "3":
        try:
            top_element = stack.peep()
            print(f"Top element is: {top_element}")
        except IndexError as e:
            print(e)
    elif choice == "4":
        print(stack.display())
    elif choice == "6":
        element_search = input("Enter the element to search in the stack: ")
        if stack.search(element_search) in stack:
            print("Yes found!")
        else:
            print("OOH No not found!")
    elif choice == "5":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please select a valid option.")




#stack.push(36)
#stack.push(84)
#stack.push(90)
#stack.push(65)
#stack.push(98)
#stack.push(43)
#print("The elements in the stack are: ", stack.display())
#print("How many elements are in the stack? ",stack.size())
#print("The first pop",stack.pop())
#print("The elements in the stack after the first pop: ", stack.display())
#print("The second pop is: ",stack.pop())
#print("The elements in the stack after the second pop: ", stack.display())
#print("The second last element is: ",stack.pop())
#print("The elements in the stack after the third pop: ", stack.display())
#print("This returns the current element with removing from stack: ",stack.peep())
#print("The elements in the stack after peeping: ", stack.display())
#print("Is our stack empty? ",stack.is_empty())
#print("How many elements are in the stack after the pop? ",stack.size())
#print(stack.search(99))
#stack.clear()
#print("The elements in the stack after clearing: ", stack.display())
#stack.delete()
#print("The elements in the stack after clearing: ", stack.display())