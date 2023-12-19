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
        
mystack = Stack()
mystack.push(23)
mystack.push(5)
mystack.push(19)
mystack.push(72)


print(mystack.peek())
print(mystack.size())