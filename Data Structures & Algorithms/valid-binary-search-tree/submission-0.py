# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isBST(root, mini, maxi):
            if not root:
                return True
            
            if not (mini < root.val < maxi):
                return False

            return isBST(root.left, mini, root.val) and isBST(root.right, root.val, maxi)


        return isBST(root, float("-inf"), float("inf"))