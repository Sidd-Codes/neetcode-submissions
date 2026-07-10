# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left = -float('inf')
        right = float('inf')
        def isValid(node, left, right):
            if node is None:
                return True
            print(node.val, left, right)
            if node.val >= right or node.val <= left:
                return False
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        return isValid(root, left, right)
