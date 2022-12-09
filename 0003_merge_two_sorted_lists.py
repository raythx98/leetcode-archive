# time: O(n)
# space: O(1)
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        prev = head = list1
        while list1 and list2:
            while list1 and list1.val <= list2.val:
                prev = list1
                list1 = list1.next
            # list1 can be None, but operations below are safe
            prev.next = shift_node = list2
            list2 = list2.next
            shift_node.next = list1
            prev = prev.next
        if list2:
            prev.next = list2
        return head