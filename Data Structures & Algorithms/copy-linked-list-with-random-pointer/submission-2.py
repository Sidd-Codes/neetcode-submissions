"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        oldtoCopy = {None:None}
        curr = head

        while curr:
            newNode = Node(curr.val)
            oldtoCopy[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldtoCopy[curr]
            copy.random = oldtoCopy[curr.random]
            copy.next = oldtoCopy[curr.next] 
            curr = curr.next
        return oldtoCopy[head]
        

