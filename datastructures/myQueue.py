#my queue

class Queue:
    def __init__(self):
        self.items =[]
    
    def dequeue(self):
        return self.items.pop()
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def isEmpty(self):
        return self.items ==[]
    
    def size(self):
        return len(self.items)
    
    
coffee_queue = Queue()

print(f"is it empty? {coffee_queue.isEmpty()}")
coffee_queue.enqueue("Paul")
coffee_queue.enqueue("Stan")
coffee_queue.enqueue("Norman")
coffee_queue.enqueue("Hugh")

print(f"is it empty? {coffee_queue.isEmpty()}")
print(f"what is the queues size then {coffee_queue.size()}")

print(f"removing {coffee_queue.dequeue()}")
print(f"what is the queues size then {coffee_queue.size()}")
