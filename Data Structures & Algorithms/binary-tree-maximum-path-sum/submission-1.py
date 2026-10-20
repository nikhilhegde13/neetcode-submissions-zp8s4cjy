# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sumMax = root.val

        def sumFinder(node):
            nonlocal sumMax
            if not node:
                return 0
            
            left = sumFinder(node.left)
            right = sumFinder(node.right)
            left = max(left, 0)
            right = max(right, 0)

            sumMax = max(sumMax, node.val + left+ right)
            return node.val + max(left, right)

        sumFinder(root)
        return sumMax