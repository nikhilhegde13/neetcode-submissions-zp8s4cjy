# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {v: i for i,v in enumerate(inorder)}


        def subTree(left, right):
            if left > right:
                return None 

            root = TreeNode(postorder.pop())
            spot = index[root.val]
            root.right = subTree(spot+1, right)
            root.left = subTree(left, spot-1)

            return root
        
        return subTree(0, len(inorder)-1)