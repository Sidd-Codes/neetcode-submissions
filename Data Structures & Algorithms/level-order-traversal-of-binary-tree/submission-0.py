# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        if root is None:
            return []
        q = deque()
        q.append(root)
        while q:
            curr = []
            for i in range(len(q)):
                c = q.popleft()
                curr.append(c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            arr.append(curr)
        return arr
