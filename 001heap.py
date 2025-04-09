class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2
    
    def _left(self, index):
        return 2 * index + 1
    
    def _right(self, index):
        return 2 * index + 2

    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)

    def _heapify_down(self, index):
        smallest = index
        left = self._left(index)
        right = self._right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[index]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[index]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def __str__(self):
        return str(self.heap)
    


    
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2
    
    def _left(self, index):
        return 2 * index + 1
    
    def _right(self, index):
        return 2 * index + 2
    
    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self._parent(index)]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)

    def _heapify_down(self, index):
        largest =index
        left = self._left(index)
        right = self._right(index)

        if left < len(self.heap) and self.heap[left] > self.heap[index]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[index]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
    
    def __str__(self):
        return str(self.heap)
            

mh = MaxHeap()
mh.push(10)
mh.push(4)
mh.push(15)
mh.push(1)
print(mh)        
print(mh.pop())  
print(mh) 