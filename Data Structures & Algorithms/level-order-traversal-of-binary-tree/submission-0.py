# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def dfs(level, root):
            if not root:
                return
            if len(ans) <= level:
                ans.append([root.val])
            else:
                ans[level].append(root.val)
            dfs(level+1, root.left)
            dfs(level+1, root.right)
        
        dfs(0,root)
        return ans
