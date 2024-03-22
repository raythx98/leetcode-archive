# time: O(n)
# space: O(1)
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class IterativeSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        advance = head.next
        prev = head
        while advance:
            prev.next = advance.next
            advance.next = head
            head = advance
            advance = prev.next
        return head
class RecursiveSolution:  
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        curr = new_head
        while curr.next:
            curr = curr.next
        curr.next = head
        head.next = None
        return new_head    
