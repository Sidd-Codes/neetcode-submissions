# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return []
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        if count - n == 0:
            return head.next
        curr = head
        for i in range(count - n):
            if i + 1 == count - n:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head