# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val 

        def maxSum(node):
            nonlocal ans
            if not node:
                return 0

            left = max(0, maxSum(node.left))
            right = max(0, maxSum(node.right))
            curr = node.val + left + right
            ans = max(ans, curr)

            return node.val + max(left, right)


        maxSum(root)
        return ans