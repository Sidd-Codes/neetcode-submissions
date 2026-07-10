# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        maxVal = -float('inf')
        q.append((root, maxVal))
        count = 0

        while q:
            currRoot, currMax = q.popleft()
            if currRoot.val >= currMax:
                count += 1
            if currRoot.left:
                q.append((currRoot.left, max(currMax, currRoot.val)))
            if currRoot.right:
                q.append((currRoot.right, max(currMax, currRoot.val)))
        return count
            

        

