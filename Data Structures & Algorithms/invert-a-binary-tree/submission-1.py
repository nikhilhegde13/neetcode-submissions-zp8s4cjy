# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def travisScott(root):
            if not root: return 
            root.left, root.right = root.right, root.left

            travisScott(root.left)
            travisScott(root.right)

        travisScott(root)

        return root