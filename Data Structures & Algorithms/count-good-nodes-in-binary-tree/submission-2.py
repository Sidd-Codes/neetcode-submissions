# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = deque()
        q.append((root, root.val))
        count = 0
        totalMax = root.val

        while q:
            curr, currMax = q.popleft()
            if curr.val >= currMax:
                count += 1
            if curr.left:
                q.append((curr.left, max(curr.val, currMax)))
            if curr.right:
                q.append((curr.right, max(curr.val, currMax)))
        return count