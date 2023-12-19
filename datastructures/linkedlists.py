#define Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data =newdata
    
    def setNext(self, newnext):
        self.next=newnext
        
    def printNode(self):
        print(self.data)


#define linked list class
class LinkedList:
    def __init__(self, newhead = None):
        self.head=newhead
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail

    def setHead(self, newhead):
        self.head = newhead
    
    def setTail(self, newtail):
        self.tail = newtail

#Task 1 - Adding a Node
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head= temp
        
#Task 2 - Removing from a Node
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
#Task 3 - Size(length) of the List
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return count

#Task 4 - Checking if an item is inthe list (Returning a boolean)
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
####################################################    
    
#print the linkedlist
    def traverse(self):
        print("Printing Linked List")
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next             

#add node at beginning
    def addAtBeginning(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp

#add node at the end
    def addAtEnd(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=temp
        
    
#####################################
# Run Program
print("Linked Lists")
LList = LinkedList()
LList.addAtBeginning("Hugh")
LList.traverse()
LList.addAtBeginning("Norman")
LList.traverse()
LList.addAtEnd("Paul")
LList.traverse()
LList.addAtBeginning("Stan")
LList.traverse()

#print(LList.getHead().data)
print(LList.length())
print(LList.search("Norman"))
LList.remove("Paul")
LList.traverse()
print("emptylsit")
newList =LinkedList()
print(newList.isEmpty())
newList.add("joe")
newList.traverse()