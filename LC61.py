'''
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
'''

from typing import Optional

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: Optional[ListNode], k:int) -> Optional[ListNode]:
    if not head or  not head.next or k==0:
        return head

    ## calculate length of list
    length = 1 
    tail = head
    while tail.next:
        tail = tail.next
        length+=1

    ## compute effective rotation
    k = k%length
    if k==0:
        return head
    
    ## go to the element to which rotation occurs or that gonna become the new head
    new_tail = head
    for _ in range(length - k -1):
        new_tail = new_tail.next

    ## break the link between new_tail and new_head
    new_head = new_tail.next
    new_tail.next = None

    ## connect the original tail with the original head
    tail.next = head

    return new_head