# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = { val: i for i,val in enumerate(inorder)}

        self.pos = 0
        def treeCreation(left, right):
            if left > right:
                return None 
            
            rootVal = preorder[self.pos]
            self.pos += 1
            root = TreeNode(rootVal)
            mid = hashmap[rootVal]
            root.left = treeCreation(left, mid-1)
            root.right = treeCreation(mid+1, right)
            return root 
        return treeCreation(0, len(inorder)-1)