'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''
from typing import Optional

class Listnode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
def reverseList(head : Optional[Listnode]) -> Optional[Listnode]:
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev