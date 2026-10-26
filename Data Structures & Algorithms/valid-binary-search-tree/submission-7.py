# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isValid(root, float("-inf"), float("inf"))

    def isValid(self, node, minVal, maxVal):
        if node is None:
            return True
        if node.val >= maxVal or node.val <= minVal:
            return False
        return self.isValid(node.left, minVal, node.val) and self.isValid(node.right, node.val, maxVal)