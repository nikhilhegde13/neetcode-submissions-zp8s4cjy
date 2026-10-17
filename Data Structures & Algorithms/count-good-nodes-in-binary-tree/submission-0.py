# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def findGood(node, localMax):
            if not node: return 0

            if node.val >= localMax: good = 1 
            else : good = 0
            localMax = max(localMax, node.val)
            
            good += findGood(node.left, localMax)
            good += findGood(node.right, localMax)
            return good
        return findGood(root, root.val)
