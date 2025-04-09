'''
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
 

Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]
'''

from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = deque(maxlen=k)
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr.append(value)
        return True       


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.arr.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.arr.pop()
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.arr[0]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.arr[-1]

    def isEmpty(self) -> bool:
        return len(self.arr) == 0

    def isFull(self) -> bool:
        return len(self.arr) == self.max_size