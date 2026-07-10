# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head

        while n > 0:
            first = first.next
            n -= 1
        prev = None
        while first:
            first = first.next
            prev = second
            second = second.next
        if prev is None:
            return head.next
        prev.next = prev.next.next
        return head