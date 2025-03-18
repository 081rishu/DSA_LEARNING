'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]
'''
from typing import Optional

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head:Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode()
    dummy_head.next = head
    curr = dummy_head

    while curr.next and curr.next.next:
        first_node = curr.next
        second_node = curr.next.next

        ##swapping
        curr.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        ##move curr
        curr = curr.next.next

    return dummy_head.next