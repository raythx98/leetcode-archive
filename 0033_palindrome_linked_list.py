# time: O(n)
# space: O(1)
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        fast = slow = head
        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next

        def reverse(curr, prev):
            while curr:
                next_n = curr.next
                curr.next = prev
                prev = curr
                curr = next_n
            return prev

        back, is_palindrome = reverse(slow.next, slow), True
        curr1, curr2 = head, back
        while curr2 != slow:
            if curr1.val != curr2.val:
                is_palindrome = False
                break
            curr1 = curr1.next
            curr2 = curr2.next

        # additional requirement: restore
        slow.next = reverse(back, None)
        return is_palindrome