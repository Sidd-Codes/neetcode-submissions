# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque([root])
        ans = []
        while q:
            lenQ = len(q)
            rightNode = None
            for i in range(lenQ):
                curr = q.popleft()
                if curr:
                    rightNode = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if rightNode:
                ans.append(rightNode.val)
        return ans