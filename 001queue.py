'''
Queue Concept
A queue is a linear data structure that follows the FIFO (First In, First Out) principle. It works like a real-world queue or line at a supermarket where the first person to join the queue is the first to be served.

Operations on Queue
Enqueue: Adds an item to the end of the queue.

Dequeue: Removes an item from the front of the queue.

Peek or Front: Returns the item at the front of the queue without removing it.

isEmpty: Checks if the queue is empty.

size: Returns the number of items in the queue.
'''

class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, val):
        self.arr.append(val)

    def dequeue(self):
        if not self.arr:
            raise IndexError("Underflow condition met")
        else:
            return self.arr.pop(0)

    def peek(self):
        if self.arr:
            return self.arr[0]
        else:
            return IndexError("No elements to show")

    def isEmpty(self):
        return len(self.arr)==0

    def size(self):
        return len(self.arr)   
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
print(q.arr)
print("<==================>")
q.dequeue()
print(f"after pop function we have the queue {q.arr}")