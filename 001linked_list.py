## node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


## linked list class using node 
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:   ## check for empty LL
            self.head = new_node
            return
        
        last = self.head     ## start with head node
        while last.next:     ## traverse to the last node while last.next is True
            last = last.next
        last.next = new_node    # link the new node to the last

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' -> ')
            temp = temp.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()
