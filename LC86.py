'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
'''

from typing import Optional

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy_head = ListNode(0)  
        dummy_head.next = head
        curr = head
        prev = dummy_head
        
        # Step 1: Move nodes < x to the front (but in reverse order)
        new_head = None  # Will store the reversed smaller elements
        while curr:
            next_node = curr.next
            if curr.val < x:
                prev.next = next_node  # Remove current node
                curr.next = new_head  # Insert at the front (reversing order)
                new_head = curr  # Move head of reversed list
            else:
                prev = curr
            curr = next_node

        # Step 2: Reverse the moved elements back to maintain order
        prev_temp = None
        curr = new_head
        while curr:
            next_node = curr.next
            curr.next = prev_temp  # Reverse
            prev_temp = curr
            curr = next_node
        
        # Step 3: Connect reversed list with remaining elements
        if prev_temp:
            temp = prev_temp
            while temp.next:  # Find the last node of reversed part
                temp = temp.next
            temp.next = dummy_head.next  # Attach the remaining part
        
        return prev_temp if prev_temp else dummy_head.next