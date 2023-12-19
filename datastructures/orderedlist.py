#Ordered Linked List
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
class OrderedList:
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        return self.head == None        

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

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return count
    
    def search(self, item):
        current = self.head
        found = False
        stop = False
        
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
                
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head=temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            
        #print the linkedlist
    def traverse(self):
        print("Printing Linked List")
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next             

#ORDERED List
print("Ordered List")
Olist = OrderedList()
print(Olist.length())
print(Olist.isEmpty())

Olist.add(8)
Olist.add(4)
Olist.add(2)
Olist.add(6)
Olist.add(4)
Olist.add(0)
Olist.add(9)
print(Olist.length())
print(Olist.isEmpty())
Olist.traverse()