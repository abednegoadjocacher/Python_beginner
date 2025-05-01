"""
Stack implementation
Operation that can be perform on stack are;
1. push()
2.pop()
3.size()
4.peek()
5.is_empty()
"""
#class Stack:
#    def __init__(self):
#        self.elements = []
#    def push(self, element):
#        self.elements.append(element)
#    def pop(self):
#        if not self.is_empty():
#           return self.elements.pop() 
#        raise IndexError("You are trying to pop an empty stack")
#    def is_empty(self):
#        return len(self.elements) == 0
#    def size(self):
#        return len(self.elements)
#    def peek(self):
#        if not self.is_empty():
#            return self.elements[-1]
#        raise IndexError("You are trying to peek into an empty stack")
#        
#stack = Stack()
#stack.push(56)
#stack.push(67)
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
#
#



#name=[]
#name.append("Prince")
#name.append("Abednego")
#name.append("Solomon")
#name.reverse()
#print(name.count())
#print(name)
#
#print(name)
#print("This will pop the last: ",name.pop())
#print(name)
#lastIn=name.pop()
#print("The second last:",lastIn)
#print("My new stack",name)
#print("This will pop the last: ",name.pop())
#print(name)
#print("This will pop the last: ",name.pop())



class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)  # Add item to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the top item
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Return the top item without removing it
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0  # Check if the stack is empty

    def size(self):
        return len(self.stack)  # Return the number of items in the stack


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
print(stack.is_empty())  # Output: False
print(stack.size())