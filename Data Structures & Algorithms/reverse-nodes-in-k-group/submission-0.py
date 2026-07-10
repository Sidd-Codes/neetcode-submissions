# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:

            node = self.getKth(groupPrev, k)
            if node is None:
                break
            groupNext = node.next
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = node
            groupPrev = temp
        return dummy.next

    def getKth(self, groupPrev, k):
        while groupPrev and k > 0:
            groupPrev = groupPrev.next
            k -= 1
        return groupPrev
