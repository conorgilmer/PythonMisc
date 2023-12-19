#dec to binary using stack

#stack datastructure
#a last in first out (LIFO)§
class Stack:
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)
        
myStack = Stack()
print(myStack.size())

original = 48
number = original

while number:
    (number, remainder) = divmod(number, 2)
    #print(remainder)
    myStack.push(remainder)

strng = ""
for i in range(myStack.size()):
    strng = strng + str(myStack.pop())
    
print(f"{original} as a binary number is {strng}")