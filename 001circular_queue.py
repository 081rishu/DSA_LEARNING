class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear+1) % self.capacity == self.front:
            print("Queue is full")
        elif self.front == -1:
            self.front = self.rear = 1
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear+1) % self.capacity
            self.queue[self.rear] = item
    
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            temp = self.queue[self.rear]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front+1) % self.capacity
            return temp
    
    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            i = self.front
            while i < self.rear:
                print(self.queue[i], end=" ")
                i = (i+1) % self.capacity
            print(self.queue[self.rear])

cq = CircularQueue(5)
cq.enqueue('A')
cq.enqueue('B')
cq.enqueue('C')
cq.enqueue('D')
cq.enqueue('E')
cq.dequeue()
cq.dequeue()
cq.enqueue('F')
cq.enqueue('G')
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.display()